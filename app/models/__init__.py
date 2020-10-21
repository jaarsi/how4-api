from peewee import SqliteDatabase, Model, DoesNotExist

# database = SqliteDatabase('database.db', pragmas={
#     'journal_mode': 'wal',
#     'cache_size': -1 * 64000,  # 64MB
#     'foreign_keys': 1,
#     'ignore_check_constraints': 0,
#     'synchronous': 0
# })

database = SqliteDatabase('database.db')

class BaseModel(Model):
	class Meta:
		database = database

from .produto import Produto

create_database = lambda: database.create_tables([Produto])