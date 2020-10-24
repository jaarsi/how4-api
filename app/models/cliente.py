from datetime import datetime
from peewee import AutoField, BooleanField, CharField, DateTimeField
from . import BaseModel

class Cliente(BaseModel):
	class Meta:
		table_name = 'tbCliente'

	id_cliente: int = AutoField(column_name='idCliente')
	no_cliente: str = CharField(column_name='noCliente', null=False)
	nu_cpf: str = CharField(column_name='nuCPF', null=False)
	de_email: str = CharField(column_name='deEmail', null=False)
	dt_cadastro: datetime = DateTimeField(column_name='dtCadastro', null=False)
	st_inativo: bool = BooleanField(column_name='stInativo', null=False, default=False)
    