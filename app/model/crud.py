import datetime
import uuid

from sqlalchemy.orm import Session

from . import models, schemas


def create_category(db: Session, name: str) -> models.Category:
    cat = models.Category(name, datetime.datetime.now())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


def read_categories(db: Session, offset: int = 0, limit: int = 100) -> int:
    count_of_rows = db.query(models.Category).offset(offset).limit(limit).all()
    return count_of_rows


# TODO: Check this function.
def update_category(db: Session, old_name: str, new_name: str) -> int:
    count_of_rows = db \
        .query(models.Category) \
        .filter(models.Category.name == old_name) \
        .update({'name': new_name}, synchronize_session=True)
    db.commit()
    db.refresh(db)
    return count_of_rows


def delete_category(db: Session, name: str) -> int:
    count_of_rows = db.query(models.Category).filter(models.Category.name == name).delete()
    return count_of_rows


def create_post(db: Session, title: str, content: str, category: str, language: str = 'english') -> models.Post:
    # Check category which actually exists.
    if db.query(models.Category).filter(models.Category.name == category).all() == 0:
        raise Exception('No Category')

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
    post = db.query(models.Post).filter(models.Post.uuid == uuid).all()
    # print(post)
    print(type(post))

    # Deal with views. TODO: Have to check this function. (update)
    if db.query(models.Post).filter(models.Post.uuid == uuid).update({'views': models.Post.views + 1}) == 0:
        raise Exception('Nothings is changed!')

    return post


def read_posts(db: Session) -> [schemas.Post]:
    posts = db.query(models.Post).all()
    # print(posts)
    print(type(posts))
    return posts


def update_post(db: Session, uuid: str, title: str, content: str, category: str) -> int:
    # Check category which actually exists.
    if db.query(models.Post).filter(models.Post.uuid == uuid).all() == 0:
        raise Exception('No category')

    # TODO: Have to check this function. (update)
    number_of_rows = db \
        .query(models.Post) \
        .filter(models.Post.uuid == uuid) \
        .update({'title': title, 'content': content, 'category': category})

    return number_of_rows


def delete_post(db: Session, uuid: str) -> int:
    number_of_rows = db.query(models.Post).filter(models.Post.uuid == uuid).delete()
    return number_of_rows


def create_user(db: Session, id: str, email: str, first_name: str, last_name: str, thumbnail_url: str):
    user = models.User(id=id, email=email, first_name=first_name, last_name=last_name, thumbnail_url=thumbnail_url)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def read_user(db: Session, id: str):
    user = db.query(models.User).filter(models.User.id == id).first()
    return user


def update_user(db: Session, email: str, first_name: str, last_name: str):
    return ''


def delete_user(db: Session, id: str):
    return ''
