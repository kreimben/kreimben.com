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
    writer = Column(String(25), ForeignKey('users.id'))


class Category(Base):
    __tablename__ = 'categories'

    name = Column(String(10), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=DateTime())


class User(Base):
    __tablename__ = 'users'

    id = Column(String(25), nullable=False, unique=True, primary_key=True)
    email = Column(String(100), nullable=True, unique=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    created_at = Column(DateTime, nullable=False, default=DateTime())
    thumbnail_url = Column(String(100), nullable=True)
