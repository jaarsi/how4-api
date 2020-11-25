from abc import ABC
from flask import jsonify, request
from ...services import CRUDService
from ...exceptions import *

class CRUDController(ABC):
    service: CRUDService

    def list(self, **kwargs):
        try:
            params = kwargs.values()
            return jsonify([ e.to_dict() for e in self.service.list(*params) ])
        except Exception as error:
            return self._handle_error(error)

    def create(self, **kwargs):
        try:
            params = kwargs.values()
            return jsonify(self.service.create(*params, data=request.json).to_dict(backrefs=True))
        except Exception as error:
            return self._handle_error(error)

    def read(self, **kwargs):
        try:
            params = kwargs.values()
            return jsonify(self.service.read(*params).to_dict(backrefs=True))
        except Exception as error:
            return self._handle_error(error)

    def update(self, **kwargs):
        try:
            params = kwargs.values()
            return jsonify(self.service.update(*params, data=request.json).to_dict(backrefs=True))
        except Exception as error:
            return self._handle_error(error)

    def delete(self, **kwargs):
        try:
            params = kwargs.values()
            return jsonify(self.service.delete(*params).to_dict())
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
            return jsonify(errors=str(error)), 500
    