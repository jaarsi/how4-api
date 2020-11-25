import os
from datetime import datetime
from playhouse.db_url import connect
from playhouse.shortcuts import model_to_dict
from peewee import (
    Model,
    AutoField,
    BooleanField,
    CharField,
    DateTimeField,
    FloatField,
    ForeignKeyField,
    IntegerField,
)

__all__ = [
    "Model", 
    "Cliente", 
    "Produto", 
    "Pedido", 
    "PedidoItem"
]

DATABASE_URL = os.getenv('DATABASE_URL')
database = connect(DATABASE_URL)
create_database = lambda: database.create_tables([Cliente, Produto, Pedido, PedidoItem])
atomic = database.atomic

class BaseModel(Model):
    class Meta:
        database = database

    def to_dict(self, **kwargs):
        return model_to_dict(self, **kwargs)


class Cliente(BaseModel):
    class Meta:
        table_name = "tbCliente"

    id_cliente: int = AutoField(column_name="idCliente")
    no_cliente: str = CharField(column_name="noCliente", null=False)
    nu_cpf: str = CharField(column_name="nuCPF", null=False)
    de_email: str = CharField(column_name="deEmail", null=False)
    dt_cadastro: datetime = DateTimeField(column_name="dtCadastro", null=False)
    st_inativo: bool = BooleanField(column_name="stInativo", null=False, default=False)


class Produto(BaseModel):
    class Meta:
        table_name = "tbProduto"

    id_produto: int = AutoField(column_name="idProduto")
    no_produto: str = CharField(column_name="noProduto", null=False)
    de_produto: str = CharField(column_name="deProduto", null=False)
    qt_estoque: int = IntegerField(column_name="qtEstoque", null=False)
    dt_cadastro: datetime = DateTimeField(column_name="dtCadastro", null=False)
    st_inativo: bool = BooleanField(column_name="stInativo", null=False, default=False)


class Pedido(BaseModel):
    class Meta:
        table_name = "tbPedido"

    id_pedido: int = AutoField(column_name="idPedido")
    cliente: Cliente = ForeignKeyField(Cliente, backref="+", column_name="idCliente")
    dt_pedido: datetime = DateTimeField(column_name="dtPedido", null=False)
    vr_pedido: float = FloatField(column_name="vrPedido", null=False)


class PedidoItem(BaseModel):
    class Meta:
        table_name = "tbPedidoItem"

    id_pedido_item: int = AutoField(column_name="idPedidoItem")
    pedido: Pedido = ForeignKeyField(Pedido, backref="itens", column_name="idPedido")
    produto: Produto = ForeignKeyField(Produto, backref="+", column_name="idProduto")
    nu_ordem: int = IntegerField(column_name="nuOrdem", null=False)
    qt_produto_item: int = IntegerField(column_name="qtProdutoItem", null=False)
    vr_unitario: float = FloatField(column_name="vrUnitario", null=False)
