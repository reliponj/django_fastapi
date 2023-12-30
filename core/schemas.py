import types
from typing import Optional

from pydantic import ConfigDict, BaseModel
from pydantic import model_validator

config = ConfigDict(from_attributes=True)


class BaseSchema(BaseModel):
    model_config = config

    @model_validator(mode='before')
    @classmethod
    def fields_t(cls, instance):
        if isinstance(instance, dict):
            return instance
        if not instance:
            return {}

        data = {}
        for name, info in cls.model_fields.items():
            attribute = getattr(instance, name)
            if isinstance(attribute, types.MethodType):
                data[name] = getattr(instance, name)()
            else:
                try:
                    queryset = getattr(instance, name).all()
                    data[name] = queryset
                except:
                    data[name] = attribute
        return data


class Response(BaseModel):
    status: bool
    message: Optional[str] = None
