from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy.orm import Session

Base = declarative_base()

factory = None


def global_init(database_path):
    global factory

    if factory:
        return

    connection_string = f"sqlite:///{database_path}"

    engine = sqlalchemy.create_engine(connection_string)
    factory = orm.sessionmaker(engine)

    from .films import Films

    Base.metadata.create_all(engine)


def create_session() -> Session:
    if factory:
        return factory()
    else:
        raise ValueError("Не инициализирована база данных")