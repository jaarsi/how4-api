from datetime import datetime
from ..models import Produto
from ..exceptions import RegraNegocioError
from .service import Service


@Service.register
class ProdutoService(Service):
    model: Produto = Produto

    @classmethod
    def create(cls, *args, data: dict):
        params = {
            "no_produto": data.get("no_produto"),
            "de_produto": data.get("de_produto"),
            "qt_estoque": data.get("qt_estoque"),
            "dt_cadastro": datetime.now(),
            "st_inativo": data.get("st_inativo"),
        }
        return super().create(*args, data=params)

    @classmethod
    def update(cls, *args, data: dict):
        params = {
            "no_produto": data.get("no_produto"),
            "de_produto": data.get("de_produto"),
            "qt_estoque": data.get("qt_estoque"),
            "st_inativo": data.get("st_inativo"),
        }
        return super().update(*args, data=params)

    @classmethod
    def validate(cls, data: dict):
        errors = []

        if data.get("no_produto", "").strip() == "":
            errors.append("O nome do produto não pode estar vazio")

        if data.get("de_produto", "").strip() == "":
            errors.append("A descrição do produto não pode estar vazia")

        if data.get("qt_estoque", 0) < 0:
            errors.append("A quantidade em estoque deve superiror a 0")

        if errors:
            raise RegraNegocioError(*errors)