from peewee import Model, PrimaryKeyField, IntegerField, CharField

class BaseModel(Model):
    class Meta:
        database = __database

class Produto(BaseModel):
    idProduto = PrimaryKeyField()
	noProduto = IntegerField(default=1, null=False)
	deProduto = CharField(null=False)