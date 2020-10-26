from flask import jsonify, request
from .services import Service
from .exceptions import DoesNotExist, IntegrityError

class Controller:
	def __init__(self, service):
		self.service: Service = service

	def list(self):
		try:
			return jsonify(self.service.list())
		except Exception as error:
			return jsonify(errors=str(error)), 500


	def create(self):
		try:
			return jsonify(self.service.create(request.json)), 201
		except IntegrityError as error:
			return jsonify(errors=error.args), 400
		except Exception as error:
			return jsonify(errors=str(error)), 500

	def read(self, id: int):
		try:
			return jsonify(self.service.read(id))
		except DoesNotExist:
			return '', 404
		except Exception as error:
			return jsonify(errors=str(error)), 500

	def update(self, id: int):
		try:
			return jsonify(self.service.update(id, request.json))
		except DoesNotExist:
			return '', 404        
		except IntegrityError as error:
			return jsonify(errors=error.args), 400
		except Exception as error:
			return jsonify(errors=str(error)), 500

	def delete(self, id: int):
		try:
			return jsonify(self.service.delete(id))                
		except DoesNotExist:
			return '', 404
		except Exception as error:
			return jsonify(errors=str(error)), 500
