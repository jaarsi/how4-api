from abc import ABC, abstractclassmethod
from app.exceptions import RegraNegocioError
from playhouse.shortcuts import model_to_dict
from .models import *

class Service(ABC):
	model: Model

	@abstractclassmethod
	def list(cls, *params):
		return [ model_to_dict(e, backrefs=True) for e in cls.model.select() ]

	@abstractclassmethod
	def create(cls, *params, data: dict):
		cls.validate(data)
		return model_to_dict(cls.model.create(**data), backrefs=True)

	@abstractclassmethod
	def read(cls, *params):
		id, = params
		return model_to_dict(cls.model.get_by_id(id), backrefs=True)

	@abstractclassmethod
	def update(cls, *params, data: dict):
		cls.validate(data)
		id, = params
		item: Model = cls.model.get_by_id(id)
		item.set_by_id(id, **data)
		return model_to_dict(item, backrefs=True)

	@abstractclassmethod
	def delete(cls, *params):
		id, = params
		item: Model = cls.model.get_by_id(id)
		item.delete_by_id(id)
		return model_to_dict(item, backrefs=True)

	@abstractclassmethod
	def validate(cls, data: dict):
		pass


class ClienteService(Service):
	model = Cliente

	@classmethod
	def validate(cls, data: dict):
		if data['no_cliente'].strip() == '':
			raise RegraNegocioError('Preencha o nome do cliente')


class ProdutoService(Service):
	model = Produto	


class EstoqueService(Service):
	model = Estoque


class PedidoService(Service):
	model = Pedido


class PedidoItemService(Service):
	model = PedidoItem	
