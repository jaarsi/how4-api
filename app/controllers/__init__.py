from ..services import ProdutoService
from .factory import controller_factory

ProdutoController = controller_factory('ProdutoController', ProdutoService)