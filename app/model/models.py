from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .database import Base


class Post(Base):
    __tablename__ = 'posts'

    uuid = Column(String(20), primary_key=True, index=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=DateTime())
    modified_at = Column(DateTime, nullable=True, default=DateTime())
    title = Column(String(200), unique=True, nullable=False)
    content = Column(String(99_999), nullable=False)
    category = Column(String(10), ForeignKey('categories.name'))
    language = Column(String(10), nullable=False)
    views = Column(Integer, nullable=False, default=1)


class Category(Base):
    __tablename__ = 'categories'

    name = Column(String(10), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=DateTime())

