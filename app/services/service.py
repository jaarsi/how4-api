from abc import ABC
from typing import Any, Dict, List
from playhouse.shortcuts import model_to_dict
from ..models import Model


class Service(ABC):
    model: Model

    @classmethod
    def list(cls, *args) -> List[Dict[str, Any]]:
        return [cls.to_dict(e) for e in cls.model.select()]

    @classmethod
    def create(cls, *args, data: dict) -> Dict[str, Any]:
        cls.validate(data)
        return cls.to_dict(cls.model.create(**data))

    @classmethod
    def read(cls, *args) -> Dict[str, Any]:
        (id,) = args
        return cls.to_dict(cls.model.get_by_id(id))

    @classmethod
    def update(cls, *args, data: dict) -> Dict[str, Any]:
        cls.validate(data)
        item = cls.read(*args)
        item.update(**data)
        cls.model.set_by_id(id, **data)
        return item

    @classmethod
    def delete(cls, *args) -> Dict[str, Any]:
        (id,) = args
        item = cls.read(*args)
        cls.model.delete_by_id(id)
        return item

    @classmethod
    def validate(cls, data: dict) -> None:
        pass

    @classmethod
    def to_dict(cls, model: Model, **kwargs) -> Dict[str, Any]:
        return model_to_dict(model, **kwargs)
