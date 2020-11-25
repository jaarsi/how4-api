from ...services import PedidoService
from . import CRUDController


@CRUDController.register
class PedidoController(CRUDController):
    service = PedidoService
