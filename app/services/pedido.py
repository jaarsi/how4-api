from datetime import datetime
from ..models import atomic, Model, Pedido
from ..exceptions import DoesNotExist, RegraNegocioError
from .service import Service
from .pedido_item import PedidoItemService
from .cliente import ClienteService


@Service.register
class PedidoService(Service):
    model: Pedido = Pedido

    @classmethod
    def create(cls, *args, data: dict):
        cls.validate(data)
        params = {
            "cliente": data.get("id_cliente"),
            "dt_pedido": datetime.now(),
            "vr_pedido": data.get("vr_pedido"),
        }

        with atomic() as tx:
            p: Pedido = cls.model.create(**params)
            for item in data['itens']:
                PedidoItemService.create(p.id_pedido, data=item)

        return cls.read(p.id_pedido)

    @classmethod
    def read(cls, *args):
        result = super().read(*args)
        result["itens"] = PedidoItemService.list(result["id_pedido"])
        return result

    @classmethod
    def update(cls, *args, data: dict):
        cls.validate(data)
        params = {
            "cliente": data.get("id_cliente"),
            "dt_pedido": datetime.now(),
            "vr_pedido": data.get("vr_pedido"),
        }

        return super().update(*args, data=params)

    @classmethod
    def to_dict(cls, model: Model, **kwargs):
        return super().to_dict(model, exclude=(
            cls.model.cliente.dt_cadastro,
            cls.model.cliente.st_inativo
        ))

    @classmethod
    def validate(cls, data: dict):
        errors = []

        try:
            ClienteService.read(data.get("id_cliente", -1))
        except DoesNotExist:
            errors.append("O cliente indicado não existe")

        if not data.get("itens"):
            errors.append("o pedido enviado não possui itens")

        if errors:
            raise RegraNegocioError(errors)