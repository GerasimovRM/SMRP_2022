from pydantic import BaseModel
from typing import Optional


class ItemIn(BaseModel):
    name: str
    description: Optional[str]


class ItemOut(ItemIn):
    id: int
