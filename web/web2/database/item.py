from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String, nullable=True)

    # users = relationship("UsersItems", back_populates="item")

