from fastapi import APIRouter, Request
from typing import List, Annotated
from fastapi import Depends, HTTPException, Form, File, UploadFile
from sqlalchemy.orm import Session
from models.photo import Photo, Base
from configs.database import engine, SessionLocal
from schema.photo import PhotoList, CreatePhoto, UpdatePhoto

router = APIRouter()
# 在資料庫中建立剛剛models中設定好的資料結構
Base.metadata.create_all(bind=engine)


# 每次操作get_db時，db使用SessionLocal中提供的資料與資料庫連線，產生db存儲，完事後關閉
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# List
@router.get("/", response_model=list[PhotoList])
def list_photo(req: Request, db: Session = Depends(get_db)):
    return db.query(Photo).all()


# Get
@router.get("/{id}", response_model=PhotoList)
def get_photo(id: int, req: Request, db: Session = Depends(get_db)):
    return db.query(Photo).get(id)


# Create
@router.post("/", response_model=PhotoList)
def create_photo(
    description: Annotated[str, Form()],
    photo: Annotated[UploadFile, File()],
    upload_time: Annotated[str, Form()],
    req: Request,
    db: Session = Depends(get_db),
):
    db_photo = Photo(photo=photo, description=description, upload_time=upload_time)
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo


# Update
@router.patch("/{id}", response_model=PhotoList)
def update_photo(
    id: int, photo: UpdatePhoto, req: Request, db: Session = Depends(get_db)
):
    db_photo = db.query(Photo).get(id)
    db_photo.photo = photo.photo
    db_photo.description = photo.description
    db_photo.upload_time = photo.upload_time
    db.commit()
    db.refresh(db_photo)
    return db_photo


# Delete
@router.delete("/{id}")
def delete_photo(id: int, req: Request, db: Session = Depends(get_db)):
    db_photo = db.query(Photo).get(id)
    db.delete(db_photo)
    db.commit()
    return None
