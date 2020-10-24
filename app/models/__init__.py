from peewee import Model, SqliteDatabase

database = SqliteDatabase(
	'database.db', 
	pragmas=(
		('journal_mode', 'wal'),
		('cache_size', -1 * 64000),
		('foreign_keys', 1),
		('ignore_check_constraints', 0),
		('synchronous', 0),
	))

class BaseModel(Model):
	class Meta:
		database = database

from .produto import Produto
from .cliente import Cliente
from .estoque import Estoque
from .pedido import Pedido
from .pedido_item import PedidoItem

create_database = lambda: database.create_tables([Cliente, Produto, Estoque, Pedido, PedidoItem])