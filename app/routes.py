from .app import app
from .controller import *

crud_endpoints = {
    'cliente': ClienteController,
    'produto': ProdutoController,
    'estoque': EstoqueController, 
    'pedido': PedidoController
}

for endpoint, ctrl in crud_endpoints.items():
    app.add_url_rule(f'/{endpoint}', f'{endpoint}_list', view_func=ctrl.list, methods=['GET',])
    app.add_url_rule(f'/{endpoint}', f'{endpoint}_create', view_func=ctrl.create, methods=['POST',])
    app.add_url_rule(f'/{endpoint}/<int:id>', f'{endpoint}_read', view_func=ctrl.read, methods=['GET',])
    app.add_url_rule(f'/{endpoint}/<int:id>', f'{endpoint}_update', view_func=ctrl.update, methods=['PUT',])
    app.add_url_rule(f'/{endpoint}/<int:id>', f'{endpoint}_delete', view_func=ctrl.delete, methods=['DELETE',])