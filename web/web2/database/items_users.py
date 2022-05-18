from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class UsersItems(Base):
    __tablename__ = "users_items"

    user_id = Column(ForeignKey("user.id"), primary_key=True)
    item_id = Column(ForeignKey("item.id"), primary_key=True)

    # user = relationship("User", back_populates="items")
    # item = relationship("Item", back_populates="users")
