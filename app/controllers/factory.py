from ..services import Service
from .controller import Controller

def initializer(service_cls):
    def f(self):
        self.service = service_cls()

    return f

def controller_factory(cls_name: str, service_cls: Service):
    return type(cls_name, (Controller,), {'__init__': initializer(service_cls)})