from abc import ABC
from datetime import datetime
from peewee import (
    SqliteDatabase,
    Model, 
    AutoField, 
    BooleanField, 
    CharField, 
    DateTimeField, 
    FloatField, 
    ForeignKeyField, 
    IntegerField
)

__all__ = [
	'Model',
	'Cliente',
	'Produto',
	'Estoque',
	'Pedido',
	'PedidoItem'
]

database = SqliteDatabase(
	'database.db', 
	pragmas=(
		('journal_mode', 'wal'),
		('cache_size', -1 * 64000),
		('foreign_keys', 1),
		('ignore_check_constraints', 0),
		('synchronous', 0),
	)
)

class BaseModel(Model):
	class Meta:
		database = database


class Cliente(BaseModel):
	class Meta:
		table_name = 'tbCliente'

	id_cliente: int = AutoField(column_name='idCliente')
	no_cliente: str = CharField(column_name='noCliente', null=False)
	nu_cpf: str = CharField(column_name='nuCPF', null=False)
	de_email: str = CharField(column_name='deEmail', null=False)
	dt_cadastro: datetime = DateTimeField(column_name='dtCadastro', null=False)
	st_inativo: bool = BooleanField(column_name='stInativo', null=False, default=False)


class Produto(BaseModel):
	class Meta:
		table_name = 'tbProduto'

	id_produto: int = AutoField(column_name='idProduto')
	no_produto: int = IntegerField(column_name='noProduto', null=False)
	de_produto: str = CharField(column_name='deProduto', null=False)
	dt_cadastro: datetime = DateTimeField(column_name='dtCadastro', null=False)
	st_inativo: bool = BooleanField(column_name='stInativo', null=False, default=False)


class Estoque(BaseModel):	
	class Meta:
		table_name = 'tbEstoque'

	id_estoque: int = AutoField(column_name='idEstoque')
	produto: Produto = ForeignKeyField(Produto, backref='estoque', column_name='idProduto', unique=True)
	qt_produto: int = IntegerField(column_name='qtProduto', null=False)
	st_inativo: bool = BooleanField(column_name='stInativo', null=False, default=False)


class Pedido(BaseModel):
	class Meta:
		table_name = 'tbPedido'

	id_pedido: int = AutoField(column_name='idPedido')
	cliente: Cliente = ForeignKeyField(Cliente, backref='pedidos', column_name='idCliente')
	dt_pedido: datetime = DateTimeField(column_name='dtPedido', null=False)
	vr_pedido: float = FloatField(column_name='vrPedido', null=False)


class PedidoItem(BaseModel):
	class Meta:
		table_name = 'tbPedidoItem'

	id_pedido_item: int = AutoField(column_name='idPedidoItem')
	pedido: Pedido = ForeignKeyField(Pedido, backref='itens', column_name='idPedido')
	produto: Produto = ForeignKeyField(Produto, column_name='idProduto')
	nu_ordem: int = IntegerField(null=False, column_name='nuOrdem')	
	qt_produto_item: int = IntegerField(null=False, column_name='qtProdutoItem')
	vr_unitario: float = FloatField(null=False, column_name='vrUnitario')
    