from proj_exceptions import InconsistentDataBaseError
from proj_extensions import db


class BaseContent(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    @classmethod
    def get(cls):
        models = cls.query.all()
        if len(models) != 1:
            raise InconsistentDataBaseError
        return models[0]
