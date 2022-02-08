from pydantic import BaseModel


class Post(BaseModel):
    id: int
    content: str
    timestamp: str

    class Config:
        orm_mode = True


class Image(BaseModel):
    id: int
    net: bytes

    class Config:
        orm_mode = True
