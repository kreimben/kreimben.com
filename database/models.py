from sqlalchemy import Column, Integer, String, BLOB
from sqlalchemy.orm import relationship

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    timestamp = Column(String, index=True)

    images = relationship("Image", back_populates="post")


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    net = Column(BLOB, index=True)

    post = relationship("Post", back_populates="images")
    