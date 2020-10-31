from datetime import datetime
from ..models import atomic, Cliente, Pedido
from ..exceptions import DoesNotExist
from .service import Service
from .pedido_item import PedidoItemService


@Service.register
class PedidoService(Service):
    model = Pedido

    @classmethod
    def create(cls, *args, data: dict):
        params = {
            "cliente": Cliente.get_by_id(data["id_cliente"]),
            "dt_pedido": datetime.now(),
            "vr_pedido": data["vr_pedido"],
        }
        items = data["itens"]

        with atomic() as tx:
            p = super().create(**params)

            for item in items:
                PedidoItemService.create(p.id_pedido, data=item)

    @classmethod
    def read(cls, *args):
        result = super().read(*args)
        result["itens"] = PedidoItemService.list(result["id_pedido"])
        return result

    @classmethod
    def update(cls, *args, data: dict):
        params = {
            "cliente": Cliente.get_by_id(data["id_cliente"]),
            "dt_pedido": datetime.now(),
            "vr_pedido": data["vr_pedido"],
        }

        with atomic() as tx:
            p: Pedido = cls.model.create(**params)
            items = data["itens"]

            for item in items:
                try:
                    PedidoItemService.update(p.id_pedido, item.id_pedido_item, data=item)
                except DoesNotExist:
                    PedidoItemService.create(p.id_pedido, data=item)
