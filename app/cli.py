from datetime import datetime
from random import randint
from .app import app
from .models import (
    create_database as create_db,
    Cliente,
    Produto,
    Pedido,
    PedidoItem,
)

@app.cli.command("create-database")
def create_database():
    try:
        create_db()
    except:
        pass


@app.cli.command("seed-database")
def seed():
    c = Cliente.create(
        no_cliente="Jairo de Araujo Silva",
        nu_cpf="13154566724",
        de_email="jairo.araujo.silva@gmail.com",
        dt_cadastro=datetime.now(),
        st_inativo=False,
    )
    p = Produto.create(
        no_produto="Camisa", 
        de_produto="Camisa", 
        dt_cadastro=datetime.now(), 
        qt_estoque=randint(1, 100), 
        st_inativo=False
    )
    ped = Pedido.create(
        cliente=c, 
        dt_pedido=datetime.now(), 
        vr_pedido=100
    )
    PedidoItem.insert_many([
        {
            "pedido": ped,
            "produto": p,
            "nu_ordem": 1,
            "qt_produto_item": 2,
            "vr_unitario": 40,
        },
        {
            "pedido": ped,
            "produto": p,
            "nu_ordem": 2,
            "qt_produto_item": 2,
            "vr_unitario": 10,
        },
    ]).execute()
