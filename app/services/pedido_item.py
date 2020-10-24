from playhouse.shortcuts import model_to_dict
from .service import Service
from ..models import PedidoItem

class PedidoItemService(Service):
    def list(self):
        return [ model_to_dict(p) for p in PedidoItem.select() ]

    def create(self, data: dict):
        return model_to_dict(PedidoItem.create(**data))

    def read(self, id: int):
        return model_to_dict(PedidoItem.get( PedidoItem.id_pedido_item == id ))

    def update(self, id: int, data: dict):
        return model_to_dict(PedidoItem.update(**data).where( PedidoItem.id_pedido_item == id))

    def delete(self, id: int):
        p: PedidoItem = PedidoItem.get( PedidoItem.id_pedido_item == id )
        p.delete_instance()
        return model_to_dict(p)
