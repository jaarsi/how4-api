from .app import app
from .services import *
from .controller import Controller

endpoints = {
    "cliente": ClienteService,
    "produto": ProdutoService,
    "estoque": EstoqueService,
    "pedido": PedidoService,
}

for endpoint, svc in endpoints.items():
    ctrl = Controller(svc)
    app.add_url_rule(f"/{endpoint}", f"{endpoint}_list", view_func=ctrl.list, methods=["GET",])
    app.add_url_rule(f"/{endpoint}", f"{endpoint}_create", view_func=ctrl.create, methods=["POST",])
    app.add_url_rule(f"/{endpoint}/<int:id>", f"{endpoint}_read", view_func=ctrl.read, methods=["GET",])
    app.add_url_rule(f"/{endpoint}/<int:id>", f"{endpoint}_update", view_func=ctrl.update, methods=["PUT",])
    app.add_url_rule(f"/{endpoint}/<int:id>", f"{endpoint}_delete", view_func=ctrl.delete, methods=["DELETE",])

ctrl = Controller(PedidoItemService)
app.add_url_rule("/pedido/<int:pedido_id>/itens", "pedido_item_list", view_func=ctrl.list, methods=["GET",])
app.add_url_rule("/pedido/<int:pedido_id>/itens", "pedido_item_create", view_func=ctrl.create, methods=["POST",])
app.add_url_rule("/pedido/<int:pedido_id>/itens/<int:id>", "pedido_item_update", view_func=ctrl.update, methods=["PUT",])
app.add_url_rule("/pedido/<int:pedido_id>/itens/<int:id>", "pedido_item_delete", view_func=ctrl.delete, methods=["DELETE",])
