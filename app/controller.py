from flask import jsonify, request
from .services import Service
from .exceptions import DoesNotExist, IntegrityError, RegraNegocioError

class Controller:
	def __init__(self, service: Service) -> None:
		self.service = service

	def list(self, **params):
		try:
			result = self.service.list(*params.values())
			return jsonify(result)
		except Exception as error:
			return jsonify(errors=str(error)), 500

	def create(self, **params):
		try:
			result = self.service.create(*params.values(), data=request.json)
			return jsonify(result), 201
		except IntegrityError as error:
			return jsonify(errors=error.args), 400
		except RegraNegocioError as error:
			return jsonify(errors=error.args), 400
		except Exception as error:
			return jsonify(errors=str(error)), 500

	def read(self, **params):
		try:
			result = self.service.read(*params.values())
			return jsonify(result)
		except DoesNotExist:
			return '', 404
		except Exception as error:
			return jsonify(errors=str(error)), 500

	def update(self, **params):
		try:
			result = self.service.update(*params.values(), data=request.json)
			return jsonify(result)
		except DoesNotExist:
			return '', 404
		except IntegrityError as error:
			return jsonify(errors=error.args), 400
		except RegraNegocioError as error:
			return jsonify(errors=error.args), 400
		except Exception as error:
			return jsonify(errors=str(error)), 500

	def delete(self, **params):
		try:
			result = self.service.delete(*params.values())
			return jsonify(result)
		except DoesNotExist:
			return '', 404
		except Exception as error:
			return jsonify(errors=str(error)), 500