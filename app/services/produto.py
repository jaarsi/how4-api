from .service import Service
from ..models import Produto


@Service.register
class ProdutoService(Service):
    model = Produto
