import re
from datetime import datetime
from ..models import Cliente
from ..exceptions import RegraNegocioError
from .service import Service


@Service.register
class ClienteService(Service):
    model: Cliente = Cliente

    @classmethod
    def create(cls, *args, data: dict):
        params = {
            "no_cliente": data["no_cliente"],
            "nu_cpf": data["nu_cpf"],
            "de_email": data["de_email"],
            "dt_cadastro": datetime.now(),
            "st_inativo": data["st_inativo"],
        }
        return super().create(*args, data=params)

    @classmethod
    def update(cls, *args, data: dict):
        params = {
            "no_cliente": data["no_cliente"],
            "nu_cpf": data["nu_cpf"],
            "de_email": data["de_email"],
            "st_inativo": data["st_inativo"],
        }
        return super().update(*args, data=params)

    @classmethod
    def validate(cls, data: dict):
        errors = {}

        if data["no_cliente"].strip() == "":
            errors["no_cliente"] = ("O nome do cliente não pode estar vazio",)

        if data["nu_cpf"].strip() == "":
            errors["nu_cpf"] = ("O CPF do cliente não pode estar vazio",)
        else:
            if not re.match("^\d{3}\.\d{3}\.\d{3}\-\d{2}$", data["nu_cpf"]):
                errors["nu_cpf"] = ("O CPF informado não é válido",)

        if data["de_email"].strip() == "":
            errors["de_email"] = ("O email do cliente não pode estar vazio",)

        if errors:
            raise RegraNegocioError(errors)
