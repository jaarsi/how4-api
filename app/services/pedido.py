from datetime import datetime
from ..models import atomic, Model, Pedido
from ..exceptions import DoesNotExist
from .service import Service
from .pedido_item import PedidoItemService


@Service.register
class PedidoService(Service):
    model: Pedido = Pedido

    @classmethod
    def create(cls, *args, data: dict):
        cls.validate(data)
        params = {
            "cliente": data["id_cliente"],
            "dt_pedido": datetime.now(),
            "vr_pedido": data["vr_pedido"],
        }

        with atomic() as tx:
            p = cls.model.create(**params)
            cls.__save_itens(p, data['itens']) 

        return cls.read(*args)

    @classmethod
    def read(cls, *args):
        result = super().read(*args)
        result["itens"] = PedidoItemService.list(result["id_pedido"])
        return result

    @classmethod
    def update(cls, *args, data: dict):
        cls.validate(data)
        params = {
            "cliente": data["id_cliente"],
            "dt_pedido": datetime.now(),
            "vr_pedido": data["vr_pedido"],
        }

        with atomic() as tx:            
            super().update(*params)
            id, = args
            p = cls.model.get(id)
            cls.__save_itens(p, data['itens'])

        return cls.read(*args)

    @classmethod
    def __save_itens(cls, pedido: Pedido, items: list):
        items = items or []
        result = []

        for item in items:
            try:
                it = PedidoItemService.update(pedido.id_pedido, item.id_pedido_item, data=item)
            except DoesNotExist:
                it = PedidoItemService.create(pedido.id_pedido, data=item)
            result.append(it)

        return result

    @classmethod
    def to_dict(cls, model: Model, **kwargs):
        return super().to_dict(model, exclude=(
            cls.model.cliente.dt_cadastro,
            cls.model.cliente.st_inativo
        ))

    @classmethod
    def validate(cls, data: dict):
        pass
