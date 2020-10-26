from playhouse.shortcuts import model_to_dict
from . import Service
from ..models import Model, Produto

class ProdutoService(Service):
    @classmethod
    def list(cls):
        return [ model_to_dict(item) for item in Produto.select() ]        

    @classmethod
    def create(cls, data: dict):
        return model_to_dict(Produto.create(**data))

    @classmethod
    def read(cls, id: int):
        return model_to_dict(Produto.get_by_id(id))

    @classmethod
    def update(cls, id: int, data: dict):
        Produto.update(**data).where(Produto.id_produto == id).execute()
        return cls.read(id)

    @classmethod
    def delete(cls, id: int):
        item = cls.read(id)
        Produto.delete().where(Produto.id_produto == id).execute()
        return item

    @classmethod
    def validate(cls, data: dict):
        pass
