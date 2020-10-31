from playhouse.shortcuts import model_to_dict
from ..models import Pedido, PedidoItem, Produto
from .service import Service


@Service.register
class PedidoItemService(Service):
    model = PedidoItem

    @classmethod
    def list(cls, *args):
        (id_pedido,) = args
        return [cls.to_dict(e) for e in cls.model.select().join(Pedido).where(Pedido.id_pedido == id_pedido)]

    @classmethod    
    def create(cls, *args, data: dict):
        id_pedido, = args
        data = {
            "pedido": Pedido.get_by_id(id_pedido),
            "produto": Produto.get_by_id(data["id_produto"]),
            "nu_ordem": 1,
            "qt_produto_item": data["qt_produto_item"],
            "vr_unitario": data["vr_unitario"],
        }
        return super().create(*args, data=data)

    @classmethod
    def update(cls, *args, data: dict):
        id_pedido, id = args
        data = {
            "produto": Produto.get_by_id(data["id_produto"]),
            "qt_produto_item": data["qt_produto_item"],
            "vr_unitario": data["vr_unitario"],
        }
        cls.model.update(**data)\
            .where(Pedido.id_pedido == id_pedido, cls.model.id_pedido_item == id)\
            .execute()
        return cls.read(id)

    @classmethod
    def delete(cls, *args) -> dict:
        id_pedido, id = args
        item = cls.read(id)
        cls.model.delete()\
            .where(Pedido.id_pedido == id_pedido, cls.model.id_pedido_item == id)\
            .execute()
        return model_to_dict(item)

    @classmethod
    def validate(cls, data: dict):
        pass
