from ..models import Model, PedidoItem
from ..exceptions import DoesNotExist, RegraNegocioError
from .service import Service
from .pedido import PedidoService
from .produto import ProdutoService


@Service.register
class PedidoItemService(Service):
    model: PedidoItem = PedidoItem

    @classmethod
    def list(cls, *args):
        id_pedido, = args
        return [ cls.to_dict(e) for e in cls.model.select().where(cls.model.pedido == id_pedido) ]

    @classmethod    
    def create(cls, *args, data: dict):
        cls.validate(data)
        id_pedido, = args
        params = {
            "pedido": id_pedido,
            "produto": data.get("id_produto"),
            "nu_ordem": 1,
            "qt_produto_item": data.get("qt_produto_item"),
            "vr_unitario": data.get("vr_unitario"),
        }
        return cls.to_dict(cls.model.create(**params))

    @classmethod
    def read(cls, *args):
        id_pedido, id_item = args
        return cls.to_dict(cls.model.get(
            cls.model.pedido == id_pedido, 
            cls.model.id_pedido_item == id_item
        ))

    @classmethod
    def update(cls, *args, data: dict):
        cls.validate(data)
        id_pedido, id_item = args
        params = {
            "pedido": id_pedido,
            "produto": data.get("id_produto"),
            "qt_produto_item": data.get("qt_produto_item"),
            "vr_unitario": data.get("vr_unitario"),
        }
        cls.model.update(**params).where(
            cls.model.pedido == id_pedido, 
            cls.model.id_pedido_item == id_item
        ).execute()
        return cls.read(id_pedido, id_item)

    @classmethod
    def delete(cls, *args) -> dict:
        id_pedido, id_item = args
        cls.model.delete().where(
            cls.model.pedido == id_pedido, 
            cls.model.id_pedido_item == id_item
        ).execute()
        return cls.read(id_pedido, id_item)

    @classmethod
    def to_dict(cls, model: Model, **kwargs):
        return super().to_dict(model, exclude=(
            cls.model.pedido,
            cls.model.produto.no_produto,
            cls.model.produto.qt_estoque,
            cls.model.produto.dt_cadastro,
            cls.model.produto.st_inativo,
        ))

    @classmethod
    def validate(cls, data: dict):
        errors = []

        try:
            produto = ProdutoService.read(data.get("id_produto", -1))

            if produto.get("qt_estoque", 0) < data.get("qt_produto_item", 0):
                errors.append("A quantidade requisitada é inferior ao estoque")
        except DoesNotExist:
            errors.append("o produto indicado não existe")

        try:
            PedidoService.read(data.get("id_pedido", -1))
        except DoesNotExist:
            errors.append("o pedido indicado no item não existe")

        if data.get("vr_unitario", 0) <= 0:
            errors.append("O valor unitário do produto deve ser positivo e maior que 0")

        if data.get("qt_produto_item", 0) <= 0:
            errors.append("A quantidade de produto deve ser positiva e maior que 0")

        if errors:
            raise RegraNegocioError(errors)
