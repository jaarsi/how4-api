from . import Service
from ..models import Produto
from ..exceptions import RegraNegocioError

class ProdutoService(Service):
    model = Produto

    @classmethod
    def validate(cls, item: Produto):
        pass
