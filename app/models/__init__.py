from peewee import SqliteDatabase, Model

database = SqliteDatabase('database.db')

class BaseModel(Model):
	class Meta:
		database = database

from .produto import Produto

create_database = lambda: database.create_tables([Produto])
