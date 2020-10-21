from peewee import AutoField, IntegerField, CharField
from . import BaseModel

class Produto(BaseModel):
	idProduto = AutoField()
	noProduto = IntegerField(null=False)
	deProduto = CharField(null=False)