from ...services import ProdutoService
from . import CRUDController


@CRUDController.register
class ProdutoController(CRUDController):
    service = ProdutoService
