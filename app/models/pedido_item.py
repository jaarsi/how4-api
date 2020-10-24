from peewee import AutoField, FloatField, ForeignKeyField, IntegerField
from . import BaseModel, Pedido, Produto

class PedidoItem(BaseModel):
	class Meta:
		table_name = 'tbPedidoItem'
		# indexes = (	(('idPedido', 'nuOrdem'), True) )

	id_pedido_item: int = AutoField(column_name='idPedidoItem')
	pedido: Pedido = ForeignKeyField(Pedido, backref='itens', column_name='idPedido')
	produto: Produto = ForeignKeyField(Produto, backref='+', column_name='idProduto')
	nu_ordem: int = IntegerField(null=False, column_name='nuOrdem')	
	qt_produto_item: int = IntegerField(null=False, column_name='qtProdutoItem')
	vr_unitario: float = FloatField(null=False, column_name='vrUnitario')
		