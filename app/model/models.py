from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from .database import Base


class Post(Base):
    __tablename__ = 'posts'

    uuid = Column(String(20), primary_key=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    modified_at = Column(DateTime(timezone=True), nullable=True, default=func.now())
    title = Column(String(200), unique=True, nullable=False)
    content = Column(String(99_999), nullable=False)
    category = Column(String(10), ForeignKey('categories.name'))
    language = Column(String(10), nullable=False)
    views = Column(Integer, nullable=False, default=1)
    writer = Column(String(25), ForeignKey('users.id'))


class Category(Base):
    __tablename__ = 'categories'

    name = Column(String(10), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), nullable=False, unique=True, primary_key=True, autoincrement=True)
    google_id = Column(String(25), nullable=False, unique=True)
    email = Column(String(100), nullable=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    thumbnail_url = Column(String(100), nullable=True)
    authorization = Column(String(10), ForeignKey('authorizations.name'))
    refresh_token = Column(String(50), nullable=True, unique=True)


class Authorization(Base):
    __tablename__ = 'authorizations'

    uuid = Column(String(20), nullable=False, unique=True, primary_key=True)
    name = Column(String(10), nullable=False, unique=True)
