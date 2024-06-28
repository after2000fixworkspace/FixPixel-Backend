from sqlalchemy.orm import Session
from models.photo import Photo
from . import models, schemas


def get_photos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Photo).offset(skip).limit(limit).all()
