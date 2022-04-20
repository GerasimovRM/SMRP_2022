from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_meta import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fio = Column(String)
    email = Column(String)

    items = relationship("Item", back_populates="user")
