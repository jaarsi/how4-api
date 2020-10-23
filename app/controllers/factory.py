from ..services import Service
from .controller import Controller

def initializer(self, service_cls):
    self.service = service_cls()

def controller_factory(cls_name: str, service_cls: Service):
    return type(cls_name, (Controller,), {'__init__': lambda self: initializer(self, service_cls)})