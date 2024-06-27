from fastapi import FastAPI

# 實體化一個 FastAPI 物件
app = FastAPI()


# 使用裝飾器定義 API 路徑及呼叫方法並套用到 root 方法上
@app.get("/")
def root():
    return "Hello world"
