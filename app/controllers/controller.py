from abc import ABC
from ..services import Service


class Controller(ABC):
    service: Service