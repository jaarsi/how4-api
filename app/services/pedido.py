from datetime import datetime
from ..models import atomic, Model, Pedido
from ..exceptions import DoesNotExist, RegraNegocioError
from .service import Service
from .cliente import ClienteService
from .pedido_item import PedidoItemService


@Service.register
class PedidoService(Service):
    model: Pedido = Pedido

    @classmethod
    def create(cls, *args, data: dict):
        params = {
            "cliente": data.get("id_cliente"),
            "dt_pedido": datetime.now(),
            "vr_pedido": data.get("vr_pedido"),
        }

        if not data.get("itens", []):
            raise RegraNegocioError("o pedido enviado não possui itens")
                
        with atomic() as tx:
            p: Pedido = super().create(*args, data=params)
            for item in data.get("itens"):
                PedidoItemService.create(p.id_pedido, data=item)

        return cls.read(p.id_pedido)

    @classmethod
    def read(cls, *args):
        result = super().read(*args)
        result["itens"] = PedidoItemService.list(result["id_pedido"])
        return result

    @classmethod
    def update(cls, *args, data: dict):
        params = {
            "cliente": data.get("id_cliente"),
            "vr_pedido": data.get("vr_pedido"),
        }

        if not data.get("itens", []):
            raise RegraNegocioError("o pedido enviado não possui itens")
        
        with atomic() as tx:
            PedidoItemService.delete_all(*args)
            p: Pedido = super().update(*args, data=params)
            for item in data.get("itens"):
                PedidoItemService.create(*args, data=item)

        return cls.read(*args)

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
            ClienteService.read(data.get("cliente", -1))
        except DoesNotExist:
            errors.append("O cliente indicado não existe")

        if errors:
            raise RegraNegocioError(*errors)