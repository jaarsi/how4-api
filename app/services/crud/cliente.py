import re
from datetime import datetime
from ...models import Cliente
from ...exceptions import RegraNegocioError
from . import CRUDService


@CRUDService.register
class ClienteService(CRUDService):
    model = Cliente

    @classmethod
    def create(cls, data: dict) -> Cliente:
        params = {
            "no_cliente": data.get("no_cliente"),
            "nu_cpf": data.get("nu_cpf"),
            "de_email": data.get("de_email"),
            "dt_cadastro": datetime.now(),
            "st_inativo": data.get("st_inativo"),
        }
        return super().create(data=params)

    @classmethod
    def update(cls, id_cliente, data: dict) -> Cliente:
        params = {
            "no_cliente": data.get("no_cliente"),
            "nu_cpf": data.get("nu_cpf"),
            "de_email": data.get("de_email"),
            "st_inativo": data.get("st_inativo"),
        }
        return super().update(id_cliente, data=params)

    @classmethod
    def validate(cls, data: dict):
        errors = []

        if data.get("no_cliente", "").strip() == "":
            errors.append("O nome do cliente não pode estar vazio")

        if data.get("nu_cpf", "").strip() == "":
            errors.append("O CPF do cliente não pode estar vazio")
        else:
            if not re.match("^\d{3}\.\d{3}\.\d{3}\-\d{2}$", data.get("nu_cpf", "")):
                errors.append("O CPF informado não é válido")

        if data.get("de_email", "").strip() == "":
            errors.append("O email do cliente não pode estar vazio")

        if errors:
            raise RegraNegocioError(*errors)
