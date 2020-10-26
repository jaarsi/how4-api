from playhouse.shortcuts import model_to_dict
from . import Service
from ..models import Cliente

class ClienteService(Service):
    @classmethod
    def list(cls):
        return [ model_to_dict(item) for item in Cliente.select() ]        

    @classmethod
    def create(cls, data: dict):
        cls.validate(data)
        return model_to_dict(Cliente.create(**data))

    @classmethod
    def read(cls, id: int):
        return model_to_dict(Cliente.get(id))

    @classmethod
    def update(cls, id: int, data: dict):
        cls.validate(data)
        return model_to_dict(Cliente.update(**data).where(Cliente.id_cliente == id))

    @classmethod
    def delete(cls, id: int):
        return model_to_dict(Cliente.delete().where(Cliente.id_cliente == id))

    @classmethod
    def validate(cls, data: dict):
        pass
