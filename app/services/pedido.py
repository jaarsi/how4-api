from . import Service
from ..models import Pedido, PedidoItem
from ..exceptions import RegraNegocioError

class PedidoService(Service):
    model = Pedido

    @classmethod
    def validate(cls, item: Pedido):
        pass

class PedidoItemService(Service):
    model = PedidoItem

    @classmethod
    def validate(cls, item: PedidoItem):
        pass