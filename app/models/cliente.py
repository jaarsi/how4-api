from peewee import AutoField, CharField
from . import BaseModel

class Cliente(BaseModel):
	idCliente: int = AutoField()
	noCliente: str = CharField(null=False)
	nuCPF: str = CharField(null=False)
	deEmail: str = CharField(null=False)
    