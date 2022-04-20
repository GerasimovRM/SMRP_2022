from pydantic import BaseModel
from typing import List
from .item import ItemOut


class UserIn(BaseModel):
    fio: str
    email: str


class UserOut(UserIn):
    id: int
    # items: List[ItemOut]
