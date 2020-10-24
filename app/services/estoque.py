from playhouse.shortcuts import model_to_dict
from .service import Service
from ..models import Estoque

class EstoqueService(Service):
    def list(self):
        return [ model_to_dict(p) for p in Estoque.select() ]

    def create(self, data: dict):
        return model_to_dict(Estoque.create(**data))

    def read(self, id: int):
        return model_to_dict(Estoque.get( Estoque.id_estoque == id ))

    def update(self, id: int, data: dict):
        return model_to_dict(Estoque.update(**data).where( Estoque.id_estoque == id))

    def delete(self, id: int):
        p: Estoque = Estoque.get( Estoque.id_estoque == id )
        p.delete_instance()
        return model_to_dict(p)
