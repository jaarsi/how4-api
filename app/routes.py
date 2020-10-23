from .app import app
from .controllers import ProdutoController

endpoints = {
    'produto': ProdutoController
}

for endpoint, controller in endpoints.items():
    c = controller().as_view('produto')
    app.add_url_rule(f'/{endpoint}', view_func=c, methods=['POST',])
    app.add_url_rule(f'/{endpoint}', view_func=c, methods=['GET',])
    app.add_url_rule(f'/{endpoint}/<int:id>', view_func=c, methods=['GET',])
    app.add_url_rule(f'/{endpoint}/<int:id>', view_func=c, methods=['PUT',])
    app.add_url_rule(f'/{endpoint}/<int:id>', view_func=c, methods=['DELETE',])
