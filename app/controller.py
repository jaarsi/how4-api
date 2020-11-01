from abc import ABC
from flask import jsonify, request
from .services import Service
from .exceptions import *

__all__ = [
    'Controller',
    'ClienteController',
    'ProdutoController',
    'PedidoController',
    'PedidoItemController',
]

class Controller(ABC):
    def __init__(self, service: Service):
        self.__service = service

    def list(self, **kwargs):
        try:
            params = kwargs.values()
            return jsonify(self.__service.list(*params))
        except Exception as error:
            return self._handle_error(error)

    def create(self, **kwargs):
        try:
            params = kwargs.values()
            data = request.json
            return jsonify(self.__service.create(*params, data=data))
        except Exception as error:
            return self._handle_error(error)

    def read(self, **kwargs):
        try:
            params = kwargs.values()
            return jsonify(self.__service.read(*params))
        except Exception as error:
            return self._handle_error(error)

    def update(self, **kwargs):
        try:
            params = kwargs.values()
            data = request.json
            return jsonify(self.__service.update(*params, data=data))
        except Exception as error:
            return self._handle_error(error)

    def delete(self, **kwargs):
        try:
            params = kwargs.values()
            return jsonify(self.__service.delete(*params))
        except Exception as error:
            return self._handle_error(error)

    def _handle_error(self, error: Exception, /):
        if isinstance(error, RegraNegocioError):
            return jsonify(errors=error.args), 400
        if isinstance(error, IntegrityError):
            return jsonify(errors=error.args), 400
        elif isinstance(error, DoesNotExist):
            return "", 404
        else:
            return jsonify(errors=error.args), 500


@Controller.register
class ClienteController(Controller):
    pass

@Controller.register
class ProdutoController(Controller):
    pass

@Controller.register
class PedidoController(Controller):
    pass

@Controller.register
class PedidoItemController(Controller):
    pass

