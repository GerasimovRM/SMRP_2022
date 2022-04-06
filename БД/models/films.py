from .base_meta import Base
from sqlalchemy import Column, Integer, String


class Films(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    # genre
    duration = Column(Integer, nullable=True)
