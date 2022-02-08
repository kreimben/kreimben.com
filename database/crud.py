from sqlalchemy.orm import Session

from . import models, schemas


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def create_post(db: Session, post: schemas.Post):
    db_post = models.Post(id = post.id, content = post.content, timestamp = post.timestamp)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_image(db: Session, image_id: int):
    return db.query(models.Image).filter(models.Image.id == image_id).first()


def create_image(db: Session, image: schemas.Image):
    db_image = models.Image(id = image.id, net = image.net)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
