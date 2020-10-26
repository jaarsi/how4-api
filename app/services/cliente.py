from . import Service
from ..models import Cliente
from ..exceptions import RegraNegocioError

class ClienteService(Service):
    model = Cliente

    def validate(cls, item: Cliente):
        if item.no_cliente.strip() == '':
            raise RegraNegocioError('O nome do cliente não pode estar vazio.')
