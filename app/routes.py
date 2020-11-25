from typing import Dict
from .app import app
from .controllers import *

crud_endpoints: Dict[str, CRUDController] = {
    "cliente": ClienteController(),
    "produto": ProdutoController(),
    "pedido": PedidoController(),
}

# generic crud routes
for endpoint, ctrl in crud_endpoints.items():
    app.add_url_rule(f"/{endpoint}", f"{endpoint}_list", view_func=ctrl.list, methods=["GET",])
    app.add_url_rule(f"/{endpoint}", f"{endpoint}_create", view_func=ctrl.create, methods=["POST",])
    app.add_url_rule(f"/{endpoint}/<int:id>", f"{endpoint}_read", view_func=ctrl.read, methods=["GET",])
    app.add_url_rule(f"/{endpoint}/<int:id>", f"{endpoint}_update", view_func=ctrl.update, methods=["PUT",])
    app.add_url_rule(f"/{endpoint}/<int:id>", f"{endpoint}_delete", view_func=ctrl.delete, methods=["DELETE",])

# others routes
app.add_url_rule(f"/dashboard", "dashboard", view_func=DashboardController.get, methods=["GET",])