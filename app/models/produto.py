from peewee import AutoField, CharField, IntegerField
from . import BaseModel

class Produto(BaseModel):
	idProduto: int = AutoField()
	noProduto: int = IntegerField(null=False)
	deProduto: str = CharField(null=False)
