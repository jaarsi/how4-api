from datetime import datetime
from ..models import Produto
from .service import Service


@Service.register
class ProdutoService(Service):
    model: Produto = Produto

    @classmethod
    def create(cls, *args, data: dict):
        params = {
            "no_produto": data["no_produto"],
            "de_produto": data["de_produto"],
            "dt_cadastro": datetime.now(),
            "st_inativo": data["st_inativo"],
        }
        return super().create(*args, data=params)

    @classmethod
    def update(cls, *args, data: dict):
        params = {
            "no_produto": data["no_produto"],
            "de_produto": data["de_produto"],
            "dt_cadastro": datetime.now(),
            "st_inativo": data["st_inativo"],
        }
        return super().update(*args, data=params)

    @classmethod
    def validate(cls, data: dict):
        pass