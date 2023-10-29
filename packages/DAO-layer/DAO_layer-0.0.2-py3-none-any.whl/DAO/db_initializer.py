from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import class_mapper
from sqlalchemy import inspect
from typing import Any, Dict

db = SQLAlchemy()
Base = declarative_base()


class DBInitializer:
    @staticmethod
    def initialize(app):
        db.init_app(app)


class ModelConverter:
    @staticmethod
    def model_to_dict(model: Any, exclude: tuple = ()) -> Dict[str, Any]:
        columns = [column.key for column in inspect(model).mapper.column_attrs]
        return {column: getattr(model, column) for column in columns if column not in exclude}
