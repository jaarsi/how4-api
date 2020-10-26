from playhouse.shortcuts import model_to_dict
from . import Service
from ..models import PedidoItem

class PedidoItemService(Service):
    @classmethod
    def list(cls):
        return [ model_to_dict(item) for item in PedidoItem.select() ]        

    @classmethod
    def create(cls, data: dict):
        return model_to_dict(PedidoItem.create(**data))

    @classmethod
    def read(cls, id: int):
        return model_to_dict(PedidoItem.get(id))

    @classmethod
    def update(cls, id: int, data: dict):
        return model_to_dict(PedidoItem.update(**data).where(PedidoItem.id_pedido == id))

    @classmethod
    def delete(cls, id: int):
        return model_to_dict(PedidoItem.delete().where(PedidoItem.id_pedido == id))

    @classmethod
    def validate(cls, data: dict):
        pass
