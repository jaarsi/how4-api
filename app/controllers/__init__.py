from ..services import *
from .factory import controller_factory

ClienteController = controller_factory('ClienteController', ClienteService)
ProdutoController = controller_factory('ProdutoController', ProdutoService)
EstoqueController = controller_factory('EstoqueController', EstoqueService)
PedidoController = controller_factory('PedidoController', PedidoService)
PedidoItemController = controller_factory('PedidoItemController', PedidoItemService)