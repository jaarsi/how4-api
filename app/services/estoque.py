from .service import Service
from ..models import Estoque


@Service.register
class EstoqueService(Service):
    model = Estoque
