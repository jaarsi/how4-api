from abc import ABC
from app.models import PedidoItem
from flask import jsonify, request
from .service import *
from .exceptions import DoesNotExist, IntegrityError, RegraNegocioError

__all__ = [
	'Controller',
	'ClienteController',
	'ProdutoController',
	'EstoqueController',
	'PedidoController',
	'PedidoItemController'
]

class Controller(ABC):
	service: Service

	@classmethod
	def list(cls):
		try:
			return jsonify(cls.service.list())
		except Exception as error:
			return jsonify(errors=str(error)), 500

	@classmethod
	def create(cls):
		try:
			return jsonify(cls.service.create(request.json)), 201
		except IntegrityError as error:
			return jsonify(errors=error.args), 400
		except RegraNegocioError as error:
			return jsonify(errors=error.args), 400
		except Exception as error:
			return jsonify(errors=str(error)), 500

	@classmethod
	def read(cls, id: int):
		try:
			return jsonify(cls.service.read(id))
		except DoesNotExist:
			return '', 404
		except Exception as error:
			return jsonify(errors=str(error)), 500

	@classmethod
	def update(cls, id: int):
		try:
			return jsonify(cls.service.update(id, request.json))
		except DoesNotExist:
			return '', 404        
		except IntegrityError as error:
			return jsonify(errors=error.args), 400
		except RegraNegocioError as error:
			return jsonify(errors=error.args), 400
		except Exception as error:
			return jsonify(errors=str(error)), 500

	@classmethod
	def delete(cls, id: int):
		try:
			return jsonify(cls.service.delete(id))                
		except DoesNotExist:
			return '', 404
		except Exception as error:
			return jsonify(errors=str(error)), 500


class ClienteController(Controller):
	service = ClienteService

class ProdutoController(Controller):
	service = ProdutoService

class EstoqueController(Controller):
	service = EstoqueService

class PedidoController(Controller):
	service = PedidoService

class PedidoItemController(Controller):
	service: Service = PedidoItemService