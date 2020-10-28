from .app import app
from .controller import Controller
from .services import *

endpoints = {
    'clientes': Controller(ClienteService),
    'produtos': Controller(ProdutoService),
    'estoques': Controller(EstoqueService), 
    'pedidos': Controller(PedidoService),
    # 'pedido_itens': Controller(PedidoService)
}

for endpoint, ctrl in endpoints.items():
    app.add_url_rule(f'/{endpoint}', f'{endpoint}_list', view_func=ctrl.list, methods=['GET',])
    app.add_url_rule(f'/{endpoint}', f'{endpoint}_create', view_func=ctrl.create, methods=['POST',])
    app.add_url_rule(f'/{endpoint}/<int:id>', f'{endpoint}_read', view_func=ctrl.read, methods=['GET',])
    app.add_url_rule(f'/{endpoint}/<int:id>', f'{endpoint}_update', view_func=ctrl.update, methods=['PUT',])
    app.add_url_rule(f'/{endpoint}/<int:id>', f'{endpoint}_delete', view_func=ctrl.delete, methods=['DELETE',])

pedido_item_ctrl = Controller(PedidoService)

app.add_url_rule(
    '/pedido/<int:pedido_id>/item', 
    'pedido_item_create', 
    view_func=pedido_item_ctrl.create, 
    methods=['POST',]
)
app.add_url_rule(
    '/pedido/<int:pedido_id>/item/<int:item_id>', 
    'pedido_item_update', 
    view_func=pedido_item_ctrl.update, 
    methods=['PUT',]
)
app.add_url_rule(
    '/pedido/<int:pedido_id>/item/<int:item_id>', 
    'pedido_item_delete', 
    view_func=pedido_item_ctrl.delete, 
    methods=['DELETE',]
)

