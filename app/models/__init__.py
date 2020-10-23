from peewee import Model, SqliteDatabase

database = SqliteDatabase('database.db')

class BaseModel(Model):
	class Meta:
		database = database

from .produto import Produto
from .cliente import Cliente

create_database = lambda: database.create_tables([Produto, Cliente])