from playhouse.shortcuts import model_to_dict
from .service import Service
from ..models import Pedido

class PedidoService(Service):
    def list(self):
        return [ model_to_dict(p) for p in Pedido.select() ]

    def create(self, data: dict):
        return model_to_dict(Pedido.create(**data))

    def read(self, id: int):
        return model_to_dict(Pedido.get( Pedido.id_pedido == id ))

    def update(self, id: int, data: dict):
        return model_to_dict(Pedido.update(**data).where( Pedido.id_pedido == id))

    def delete(self, id: int):
        p: Pedido = Pedido.get( Pedido.id_pedido == id )
        p.delete_instance()
        return model_to_dict(p)
