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
            cls.create_items(pedido, items)
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
            PedidoItem.delete().where(PedidoItem.pedido == id_pedido).execute()
            cls.create_items(id_pedido, items)
            return cls.read(id_pedido)

    @classmethod
    def delete(cls, id_pedido) -> dict:
        with atomic():
            PedidoItem.delete().where(PedidoItem.pedido == id_pedido).execute()
            return super().delete(id_pedido)

    @classmethod
    def create_items(cls, pedido, items: list):
        for item in items:
            cls.create_item(pedido, item)

    @classmethod
    def create_item(cls, pedido, item: dict):
        params = {
            "nu_ordem": item.get("nu_ordem", 1),
            "produto": item.get("produto", -1),
            "qt_produto_item": item.get("qt_produto_item"),
            "vr_unitario": item.get("vr_unitario")
        }
        return PedidoItem.create(pedido=pedido, **params)

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
            for item in items:
                try:
                    produto: Produto = Produto.get_by_id(item.get("produto", -1))
                    if produto.qt_estoque < item.get("qt_produto_item", 0):
                        errors.append(f"Item {item['nu_ordem']}: A quantidade requisitada é inferior ao estoque")
                except DoesNotExist:
                    errors.append(f"Item {item['nu_ordem']}: O produto indicado não existe")

                if item.get("vr_unitario", 0) <= 0:
                    errors.append(f"Item {item['nu_ordem']}: O valor unitário do produto deve ser positivo e maior que 0")

                if item.get("qt_produto_item", 0) <= 0:
                    errors.append(f"Item {item['nu_ordem']}: A quantidade de produto deve ser positiva e maior que 0")

        if errors:
            raise RegraNegocioError(*errors)
