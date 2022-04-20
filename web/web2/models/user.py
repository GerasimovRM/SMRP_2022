from pydantic import BaseModel
from typing import List, Optional
from .item import ItemOut


class UserIn(BaseModel):
    fio: str
    email: str


class UserOut(UserIn):
    id: int
    # items: List[ItemOut]


class UserPut(BaseModel):
    id: int
    fio: Optional[str]
    email: Optional[str]
