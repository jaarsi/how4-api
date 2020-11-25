from abc import ABC
from typing import List
from ...models import BaseModel


class CRUDService(ABC):
    model: BaseModel

    @classmethod
    def list(cls) -> List[BaseModel]:
        return [ e for e in cls.model.select() ]

    @classmethod
    def create(cls, data: dict) -> BaseModel:
        cls.validate(data)
        return cls.model.create(**data)

    @classmethod
    def read(cls, id: int) -> BaseModel:
        return cls.model.get_by_id(id)

    @classmethod
    def update(cls, id: int, data: dict) -> BaseModel:
        cls.validate(data)
        cls.model.set_by_id(id, data)
        return cls.read(id)

    @classmethod
    def delete(cls, id: int) -> BaseModel:
        item = cls.read(id)
        cls.model.delete_by_id(id)
        return item

    @classmethod
    def validate(cls, data: dict):
        pass
