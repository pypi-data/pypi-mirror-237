from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import class_mapper
from sqlalchemy import inspect

db = SQLAlchemy()
Base = declarative_base()


def init_db(app):
    db.init_app(app)


def model_to_dict(model, exclude=()):
    columns = [column.key for column in inspect(model).mapper.column_attrs]
    return {column: getattr(model, column) for column in columns if column not in exclude}
