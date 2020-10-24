from peewee import AutoField, BooleanField, IntegerField, ForeignKeyField
from . import BaseModel, Produto

class Estoque(BaseModel):	
	class Meta:
		table_name = 'tbEstoque'

	id_estoque: int = AutoField(column_name='idEstoque')
	produto: Produto = ForeignKeyField(Produto, backref='estoque', column_name='idProduto', unique=True)
	qt_produto: int = IntegerField(column_name='qtProduto', null=False)
	st_inativo: bool = BooleanField(column_name='stInativo', null=False, default=False)
	