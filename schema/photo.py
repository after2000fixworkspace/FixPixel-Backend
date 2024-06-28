from typing import Optional
from fastapi import UploadFile
from pydantic import BaseModel
from datetime import datetime


class CreatePhoto(BaseModel):
    photo: UploadFile
    description: str
    upload_time: datetime

    class Config:
        orm_mode = True


class UpdatePhoto(BaseModel):
    photo: str
    description: str
    upload_time: datetime

    class Config:
        orm_mode = True


class PhotoList(BaseModel):
    id: int
    photo: str
    description: str
    upload_time: datetime

    class Config:
        orm_mode = True
