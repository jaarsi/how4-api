from playhouse.shortcuts import model_to_dict
from . import Service
from ..models import Estoque

class EstoqueService(Service):
    @classmethod
    def list(cls):
        return [ model_to_dict(item) for item in Estoque.select() ]        

    @classmethod
    def create(cls, data: dict):
        return model_to_dict(Estoque.create(**data))

    @classmethod
    def read(cls, id: int):
        return model_to_dict(Estoque.get(id))

    @classmethod
    def update(cls, id: int, data: dict):
        return model_to_dict(Estoque.update(**data).where(Estoque.id_estoque == id))

    @classmethod
    def delete(cls, id: int):
        return model_to_dict(Estoque.delete().where(Estoque.id_estoque == id))

    @classmethod
    def validate(cls, data: dict):
        pass
