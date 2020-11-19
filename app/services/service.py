from abc import ABC
from playhouse.shortcuts import model_to_dict
from ..models import Model


class Service(ABC):
    model: Model

    @classmethod
    def list(cls, *args):
        return [ cls.to_dict(e) for e in cls.model.select() ]

    @classmethod
    def create(cls, *args, data: dict):
        cls.validate(data)
        return cls.to_dict(cls.model.create(**data))

    @classmethod
    def read(cls, *args):
        id, = args
        return cls.to_dict(cls.model.get_by_id(id))

    @classmethod
    def update(cls, *args, data: dict):
        cls.validate(data)
        id, = args
        cls.model.set_by_id(id, data)
        return cls.read(id)

    @classmethod
    def delete(cls, *args):
        id, = args
        item = cls.read(id)
        cls.model.delete_by_id(id)
        return item

    @classmethod
    def to_dict(cls, model: Model, **kwargs):
        return model_to_dict(model, **kwargs)

    @classmethod
    def validate(cls, data: dict):
        pass
