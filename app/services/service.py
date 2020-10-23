from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, data: dict):
        pass

    @abstractmethod
    def read(self, id: int):
        pass

    @abstractmethod
    def update(self, id: int, data: dict):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
