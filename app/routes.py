from typing import Dict
from .app import app
from .services import *
from .controller import *

endpoints: Dict[str, Controller] = {
    "cliente": ClienteController(ClienteService),
    "produto": ProdutoController(ProdutoService),
    "pedido": PedidoController(PedidoService),
}

# Generic CRUD routes
for endpoint, ctrl in endpoints.items():
    app.add_url_rule(f"/{endpoint}", f"{endpoint}_list", view_func=ctrl.list, methods=["GET",])
    app.add_url_rule(f"/{endpoint}", f"{endpoint}_create", view_func=ctrl.create, methods=["POST",])
    app.add_url_rule(f"/{endpoint}/<int:id>", f"{endpoint}_read", view_func=ctrl.read, methods=["GET",])
    app.add_url_rule(f"/{endpoint}/<int:id>", f"{endpoint}_update", view_func=ctrl.update, methods=["PUT",])
    app.add_url_rule(f"/{endpoint}/<int:id>", f"{endpoint}_delete", view_func=ctrl.delete, methods=["DELETE",])