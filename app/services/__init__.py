from abc import ABC, abstractclassmethod

class Service(ABC):
    @abstractclassmethod
    def list(cls):
        pass

    @abstractclassmethod
    def create(cls, data: dict):
        pass

    @abstractclassmethod
    def read(cls, id: int):
        pass

    @abstractclassmethod
    def update(cls, id: int, data: dict):
        pass

    @abstractclassmethod
    def delete(cls, id: int):
        pass        

    @abstractclassmethod
    def validate(cls, data: dict):
        pass

from .cliente import ClienteService
from .produto import ProdutoService
from .estoque import EstoqueService
from .pedido import PedidoService
from .pedido_item import PedidoItemService
