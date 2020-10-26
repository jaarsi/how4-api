from abc import ABC
from playhouse.shortcuts import model_to_dict, dict_to_model
from .exceptions import RegraNegocioError
from .models import *

__all__ = [
    'Service',
    'ClienteService',
    'ProdutoService',
    'EstoqueService',
    'PedidoService',
    'PedidoItemService'
]

class Service(ABC):
    model: Model
    
    @classmethod
    def list(cls):
        return [ model_to_dict(item) for item in cls.model.select() ]

    @classmethod
    def create(cls, data: dict):
        item: Model = dict_to_model(cls.model, data)
        cls.validate(cls, item)
        item.save()
        return model_to_dict(item)

    @classmethod
    def read(cls, id: int):
        return model_to_dict(cls.model.get_by_id(id))

    @classmethod
    def update(cls, id: int, data: dict):
        item: Model = dict_to_model(cls.model, data)
        cls.validate(item)
        cls.model.update(**data).where(cls.model._meta.primary_key == id)
        return cls.read(id)

    @classmethod
    def delete(cls, id: int):
        item = cls.read(id)
        cls.model.delete_by_id(id)
        return item

    @classmethod
    def validate(cls, item: Model):
        pass

class ClienteService(Service):
    model = Cliente

class ProdutoService(Service):
    model = Produto

class EstoqueService(Service):
    model = Estoque

class PedidoService(Service):
    model = Pedido

class PedidoItemService(Service):
    model = PedidoItem
