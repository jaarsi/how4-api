from datetime import datetime
from peewee import AutoField, BooleanField, CharField, DateTimeField, IntegerField
from . import BaseModel

class Produto(BaseModel):
	class Meta:
		table_name = 'tbProduto'

	id_produto: int = AutoField(column_name='idProduto')
	no_produto: int = IntegerField(column_name='noProduto', null=False)
	de_produto: str = CharField(column_name='deProduto', null=False)
	dt_cadastro: datetime = DateTimeField(column_name='dtCadastro', null=False)
	st_inativo: bool = BooleanField(column_name='stInativo', null=False, default=False)

