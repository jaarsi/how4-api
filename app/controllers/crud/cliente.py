from ...services import ClienteService
from . import CRUDController


@CRUDController.register
class ClienteController(CRUDController):
    service = ClienteService
    
