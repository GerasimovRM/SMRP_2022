from pydantic import BaseModel
from typing import List, Optional
from .item import ItemOut


class UserIn(BaseModel):
    fio: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    fio: str
    email: str
    items: Optional[List[ItemOut]]

    class Config:
        orm_mode = True


class UserPut(BaseModel):
    id: int
    fio: Optional[str]
    email: Optional[str]
