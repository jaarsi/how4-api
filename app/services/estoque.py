from . import Service
from ..models import Estoque
from ..exceptions import RegraNegocioError

class EstoqueService(Service):
    model = Estoque

    @classmethod
    def validate(cls, item: Estoque):
        pass