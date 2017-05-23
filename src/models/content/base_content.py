from proj_exceptions import InconsistentDataBaseError
from models.base import BaseModel


class BaseContent(BaseModel):
    __abstract__ = True

    @classmethod
    def get(cls):
        models = cls.query.all()
        if len(models) != 1:
            raise InconsistentDataBaseError
        return models[0]
