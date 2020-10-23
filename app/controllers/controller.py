from app.services import service
from flask import jsonify, request
from flask.views import MethodView
from ..exceptions import DoesNotExist, IntegrityError
from ..services import Service

class Controller(MethodView):
    def __init__(self, service):
        self.service: Service = service

    def post(self):
        try:
            return jsonify(self.service.create(request.json)), 201
        except IntegrityError as error:
            return jsonify(errors=error.args), 400

    def get(self, id: int=None):
        try:
            result = id and self.service.read(id) or self.service.list()
        except DoesNotExist:
            return '', 404
        else:
            return jsonify(result)

    def put(self, id: int):
        try:
            return jsonify(self.service.update(id, request.json))
        except DoesNotExist:
            return '', 404        
        except IntegrityError as error:
            return jsonify(errors=error.args), 400

    def delete(self, id: int):
        try:
            return jsonify(self.service.delete(id))                
        except DoesNotExist:
            return '', 404
