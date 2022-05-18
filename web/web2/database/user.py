from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_meta import Base
from .items_users import UsersItems

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fio = Column(String)
    email = Column(String)
    password = Column(String(1000), nullable=True)

    items = relationship("Items",
                         secondary=UsersItems,
                         backref="users")
    # items = relationship("UsersItems", back_populates="user")
