from pydantic import BaseModel
from typing import List, Optional


# pydantic >> 데이터 유효성 검증
class ItemBase(BaseModel):
    title: str
    description: str

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True  # orm 방식으로 데이터 필드 읽기가 가능

class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    title: Optional[str] = None
    description: Optional[str] = None


class UserBase(BaseModel):
    email: str


class User(BaseModel):
    id: int
    email: str

    items: List[Item] = []

    class Config:
        orm_mode = True  # orm 방식으로 데이터 필드 읽기가 가능


class UserCreate(UserBase):
    hashed_password: str





class UserUpdate(UserBase):
    # |(or)는 파이썬 3.10이후 부터 가능
    # email: str | None = None
    # password: str | None = None
    # 아래 방법은 3.10이전 방법
    email: Optional[str] = None
    hashed_password: Optional[str] = None
