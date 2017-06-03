from models.base import BaseModel
from proj_exceptions import InconsistentDataBaseError


class BaseContent(BaseModel):
    __abstract__ = True

    # noinspection PyMethodOverriding
    @classmethod
    def get(cls):
        models = cls.query.all()
        if len(models) != 1:
            raise InconsistentDataBaseError
        return models[0]
