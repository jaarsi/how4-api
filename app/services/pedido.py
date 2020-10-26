from playhouse.shortcuts import model_to_dict
from . import Service
from ..models import Pedido

class PedidoService(Service):
    @classmethod
    def list(cls):
        return [ model_to_dict(item) for item in Pedido.select() ]        

    @classmethod
    def create(cls, data: dict):
        return model_to_dict(Pedido.create(**data))

    @classmethod
    def read(cls, id: int):
        return model_to_dict(Pedido.get(id))

    @classmethod
    def update(cls, id: int, data: dict):
        return model_to_dict(Pedido.update(**data).where(Pedido.id_pedido == id))

    @classmethod
    def delete(cls, id: int):
        return model_to_dict(Pedido.delete().where(Pedido.id_pedido == id))

    @classmethod
    def validate(cls, data: dict):
        pass
