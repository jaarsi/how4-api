from .app import app
from .controllers import *

endpoints = {
    'cliente': ClienteController,
    'produto': ProdutoController,
    'estoque': EstoqueController,
    'pedido': PedidoController,
    # 'pedido_item': PedidoItemController
}

for endpoint, controller_cls in endpoints.items():
    c = controller_cls().as_view(endpoint)
    app.add_url_rule(f'/{endpoint}', view_func=c, methods=['GET',])
    app.add_url_rule(f'/{endpoint}', view_func=c, methods=['POST',])
    app.add_url_rule(f'/{endpoint}/<int:id>', view_func=c, methods=['GET',])
    app.add_url_rule(f'/{endpoint}/<int:id>', view_func=c, methods=['PUT',])
    app.add_url_rule(f'/{endpoint}/<int:id>', view_func=c, methods=['DELETE',])
