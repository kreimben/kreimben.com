from datetime import datetime
from pydantic import BaseModel


class Post(BaseModel):
    uuid: str
    created_at: datetime
    modified_at: datetime
    title: str
    content: str
    category: str
    language: str
    views: int

    class Config:
        orm_mode = True


class Category(BaseModel):
    name: str
    created_at: datetime

    class Config:
        orm_mode = True
