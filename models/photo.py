from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime
from configs.database import Base
from fastapi_storages.integrations.sqlalchemy import FileType
from fastapi_storages import FileSystemStorage

storage = FileSystemStorage(path="./media/fast-image")


# 建立class並繼承Base，設定存入的tablename，並設定PK，還有各個column存入的資料形態
class Photo(Base):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True, index=True)
    photo = Column(FileType(storage=storage))
    description = Column(String)
    upload_time = Column(DateTime)
