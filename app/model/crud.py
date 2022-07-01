import datetime
import uuid

from sqlalchemy.orm import Session

import app.utils.errors as errors
from . import models, schemas


def create_category(db: Session, name: str) -> models.Category:
    category = models.Category(name, datetime.datetime.now())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def read_categories(db: Session, name: str) -> int:
    category = db.query(models.Category).filter(models.Category.name == name).first()
    if not category:
        raise errors.DBError('Nothing Updated!')
    return category


def update_category(db: Session, old_name: str, new_name: str) -> int:
    number_of_rows = db \
        .query(models.Category) \
        .filter(models.Category.name == old_name) \
        .update({'name': new_name}, synchronize_session=True)
    if number_of_rows == 0:
        raise errors.DBError('Nothing Updated!')
    db.commit()
    return number_of_rows


def delete_category(db: Session, name: str) -> int:
    number_of_rows = db.query(models.Category).filter(models.Category.name == name).delete()
    if number_of_rows == 0:
        raise errors.DBError('Nothing Deleted!')
    elif number_of_rows > 1:
        raise errors.DBError('Many Rows Are Going To Deleted.')
    db.commit()
    return number_of_rows


def create_post(db: Session, title: str, content: str, category: str, language: str = 'english') -> models.Post:
    # Check category which actually exists.
    if not db.query(models.Category).filter(models.Category.name == category).first():
        raise errors.DBError('No Such Category')

    post = models.Post(
        uuid=str(uuid.uuid4()),  # Generate random uuid.
        created_at=datetime.datetime.now(),
        title=title,
        content=content,
        category=category,
        language=language
    )

    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def read_post(db: Session, uuid: str) -> schemas.Post:
    post = db.query(models.Post).filter(models.Post.uuid == uuid).first()
    return post


def read_posts(db: Session) -> [schemas.Post]:
    posts = db.query(models.Post).all()
    return posts


def update_post(db: Session, uuid: str, title: str, content: str, category: str) -> int:
    # Check category which actually exists.
    if not db.query(models.Post).filter(models.Post.uuid == uuid).first():
        raise errors.DBError('No category')

    number_of_rows = db \
        .query(models.Post) \
        .filter(models.Post.uuid == uuid) \
        .update({'title': title, 'content': content, 'category': category})
    db.commit()
    return number_of_rows


def delete_post(db: Session, uuid: str) -> int:
    number_of_rows = db.query(models.Post).filter(models.Post.uuid == uuid).delete()
    if number_of_rows == 0:
        raise errors.DBError('Nothing Deleted.')
    elif number_of_rows > 1:
        raise errors.DBError('Many Rows Are Going To Deleted.')
    db.commit()
    return number_of_rows


def create_user(db: Session,
                google_id: str,
                email: str,
                first_name: str,
                last_name: str,
                thumbnail_url: str,
                authorization: str = 'member'):
    # Check authorization first.
    if len(db.query(models.Authorization).filter(models.Authorization.name == authorization).all()) == 0:
        raise errors.DBError('No Such Authorization.')

    # Check user first.
    if len(db.query(models.User).filter(models.User.google_id == google_id).all()) != 0:
        raise errors.DBError('Already User Exists.')

    # Create user model.
    user = models.User(google_id=google_id,
                       email=email,
                       first_name=first_name,
                       last_name=last_name,
                       thumbnail_url=thumbnail_url,
                       authorization=authorization)

    if not user:
        raise errors.DBError('User Not Created.')

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def read_user(db: Session,
              google_id: str | None = None,
              refresh_token: str | None = None,
              user_id: str | None = None
              ) -> models.User:
    if google_id is not None:
        user = db.query(models.User).filter(models.User.google_id == google_id).first()
    elif refresh_token is not None:
        user = db.query(models.User).filter(models.User.refresh_token == refresh_token).first()
    elif user_id is not None:
        user = db.query(models.User).filter(models.User.user_id == user_id).first()

    if not user:
        raise errors.DBError('No Such User.')
    return user


def read_users(db: Session) -> [models.User]:
    return db.query(models.User).all()


def update_user(db: Session,
                user_id: str, email: str, first_name: str, last_name: str, refresh_token: str | None) -> int:
    number_of_rows = db.query(models.User) \
        .filter(models.User.user_id == user_id) \
        .update({'email': email,
                 'first_name': first_name,
                 'last_name': last_name,
                 'refresh_token': refresh_token})
    if not number_of_rows:
        raise errors.DBError('Nothing Updated.')
    db.commit()
    return number_of_rows


def delete_user(db: Session, user_id: str):
    number_of_rows = db.query(models.User).filter(models.User.user_id == user_id).delete()
    if number_of_rows == 0:
        raise errors.DBError('Nothing Deleted.')
    elif number_of_rows > 1:
        raise errors.DBError('Many Rows Are Going To Deleted.')
    db.commit()
    return number_of_rows


def create_authorization(db: Session, name: str):
    # Check first those name's authorizations.
    if len(db.query(models.Authorization).filter(models.Authorization.name == name).all()) != 0:
        raise errors.DBError('Already Authorization Exists.')

    auth = models.Authorization(uuid=str(uuid.uuid4()), name=name)
    db.add(auth)
    db.commit()
    db.refresh(auth)

    return auth


def read_authorization(db: Session, name: str):
    auth = db.query(models.Authorization).filter(models.Authorization.name == name).first()
    if not auth:
        raise errors.DBError('No Such Authorization.')
    return auth


def read_authorizations(db: Session, name: str):
    auths = db.query(models.Authorization).filter(models.Authorization.name == name).all()
    if len(auths) == 0:
        raise errors.DBError('No Authorizations.')
    return auths


def update_authorization(db: Session, old_name: str, new_name: str):
    number_of_rows = db.query(models.Authorization).filter(models.Authorization.name == old_name).update(
        {'name': new_name})
    if number_of_rows == 0:
        raise errors.DBError('Nothing Updated.')
    db.commit()
    return number_of_rows


def delete_authorization(db: Session, name: str) -> int:
    number_of_rows = db.query(models.Authorization).filter(models.Authorization.name == name).delete()
    if number_of_rows == 0:
        raise errors.DBError('Nothing Deleted.')
    elif number_of_rows > 1:
        raise errors.DBError('Many Rows Are Going To Deleted.')
    db.commit()
    return number_of_rows
