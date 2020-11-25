from datetime import datetime
from ...models import Produto, atomic, Pedido, PedidoItem
from ...exceptions import DoesNotExist, RegraNegocioError
from . import CRUDService
from .cliente import ClienteService


@CRUDService.register
class PedidoService(CRUDService):
    model = Pedido

    @classmethod
    def create(cls, data: dict) -> Pedido:
        params = {
            "cliente": data.get("cliente"),
            "dt_pedido": datetime.now(),
            "vr_pedido": data.get("vr_pedido"),
            "itens": data.get("itens", [])            
        }

        cls.validate(params)
        items = params.pop('itens', [])

        with atomic():
            pedido = Pedido.create(**params)
            cls.add_items(pedido, items)
            cls.update_items_stock(items)            
            return cls.read(pedido.id_pedido)

    @classmethod
    def update(cls, id_pedido, data: dict) -> Pedido:
        params = {
            "cliente": data.get("cliente"),
            "vr_pedido": data.get("vr_pedido"),
            "itens": data.get("itens", [])
        }

        cls.validate(params)
        items = params.pop('itens', [])

        with atomic() as tx:            
            Pedido.set_by_id(id_pedido, params)
            cls.restock(id_pedido)
            cls.remove_all_items(id_pedido)
            cls.add_items(id_pedido, items)
            cls.update_items_stock(items)
            return cls.read(id_pedido)

    @classmethod
    def delete(cls, id_pedido) -> dict:
        with atomic():
            cls.remove_all_items(id_pedido)
            return super().delete(id_pedido)

    @classmethod
    def add_items(cls, pedido, items: list):
        for i, item in enumerate(items, 1):
            item["nu_ordem"] = i
            item_pedido = cls.add_item(pedido, item)
            

    @classmethod
    def add_item(cls, pedido, item: dict):
        params = {
            "pedido": pedido,
            "nu_ordem": item.get("nu_ordem", 1),
            "produto": item.get("produto", -1),
            "qt_produto_item": item.get("qt_produto_item", 0),
            "vr_unitario": item.get("vr_unitario", 0)
        }
        return PedidoItem.create(**params)

    @classmethod
    def update_items_stock(cls, items: list):
        for item in items:
            p: Produto = Produto.get(item.get("produto", 0))
            p.qt_estoque -= item.get("qt_produto_item", 0)
            p.save()

    @classmethod
    def restock(cls, id_pedido):
        pedido: Pedido = Pedido.get(id_pedido)

        for item in pedido.itens:
            p: Produto = Produto.get(item.produto.id_produto)
            p.qt_estoque += item.qt_produto_item
            p.save()

    @classmethod
    def remove_all_items(cls, id_pedido):
        PedidoItem.delete().where(PedidoItem.pedido == id_pedido).execute()

    @classmethod
    def validate(cls, data: dict):
        errors = []

        try:
            ClienteService.read(data.get("cliente", -1))
        except DoesNotExist:
            errors.append("O cliente indicado não existe")

        if not (items := data.get("itens", [])):
            errors.append("O pedido enviado não possui itens")
        else:
            for i, item in enumerate(items, 1):
                try:
                    produto: Produto = Produto.get_by_id(item.get("produto", -1))
                    if produto.qt_estoque < item.get("qt_produto_item", 0):
                        errors.append(f"Item {i}: A quantidade requisitada é inferior ao estoque")
                except DoesNotExist:
                    errors.append(f"Item {i}: O produto indicado não existe")

                if item.get("vr_unitario", 0) <= 0:
                    errors.append(f"Item {i}: O valor unitário do produto deve ser positivo e maior que 0")

                if item.get("qt_produto_item", 0) <= 0:
                    errors.append(f"Item {i}: A quantidade de produto deve ser positiva e maior que 0")

        if errors:
            raise RegraNegocioError(*errors)
