from fastapi import FastAPI, Depends, HTTPException
from models import photo
from typing import List, Annotated
from controllers import photo

# 引入engine及database設定好的SessionLocal


# 引入Session
from sqlalchemy.orm import Session

# 實體化一個 FastAPI 物件
app = FastAPI()
app.include_router(router=photo.router, prefix="/photo", tags=["photo"])

@app.get("/")
def root():
    return "Hello world"
