from datetime import datetime
from peewee import AutoField, DateTimeField, FloatField, ForeignKeyField
from . import BaseModel, Cliente

class Pedido(BaseModel):
	class Meta:
		table_name = 'tbPedido'

	id_pedido: int = AutoField(column_name='idPedido')
	cliente: Cliente = ForeignKeyField(Cliente, backref='pedidos', column_name='idCliente')
	dt_pedido: datetime = DateTimeField(column_name='dtPedido', null=False)
	vr_pedido: float = FloatField(column_name='vrPedido', null=False)
        