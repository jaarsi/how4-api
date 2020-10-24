from playhouse.shortcuts import model_to_dict
from .service import Service
from ..models import Cliente

class ClienteService(Service):
    def list(self):
        return [ model_to_dict(p) for p in Cliente.select() ]

    def create(self, data: dict):
        return model_to_dict(Cliente.create(**data))

    def read(self, id: int):
        return model_to_dict(Cliente.get( Cliente.id_cliente == id ))

    def update(self, id: int, data: dict):
        return model_to_dict(Cliente.update(**data).where( Cliente.id_cliente == id))

    def delete(self, id: int):
        p: Cliente = Cliente.get( Cliente.id_cliente == id )
        p.delete_instance()
        return model_to_dict(p)
