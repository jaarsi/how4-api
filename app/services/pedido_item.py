from ..models import Model, PedidoItem
from .service import Service


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
            "produto": data["id_produto"],
            "nu_ordem": 1,
            "qt_produto_item": data["qt_produto_item"],
            "vr_unitario": data["vr_unitario"],
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
            "produto": data["id_produto"],
            "qt_produto_item": data["qt_produto_item"],
            "vr_unitario": data["vr_unitario"],
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
        pass
