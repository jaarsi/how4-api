from datetime import datetime
from ...models import Produto
from ...exceptions import RegraNegocioError
from . import CRUDService


@CRUDService.register
class ProdutoService(CRUDService):
    model = Produto

    @classmethod
    def create(cls, data: dict) -> Produto:
        params = {
            "no_produto": data.get("no_produto"),
            "de_produto": data.get("de_produto"),
            "qt_estoque": data.get("qt_estoque"),
            "dt_cadastro": datetime.now(),
            "st_inativo": data.get("st_inativo"),
        }
        return super().create(data=params)

    @classmethod
    def update(cls, id_produto, data: dict) -> Produto:
        params = {
            "no_produto": data.get("no_produto"),
            "de_produto": data.get("de_produto"),
            "qt_estoque": data.get("qt_estoque"),
            "st_inativo": data.get("st_inativo"),
        }
        return super().update(id_produto, data=params)

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