# Sample example code taken from https://fastapi.tiangolo.com/

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel   # ← 追加

import uvicorn

app = FastAPI()

# POSTで受け取るデータの形を定義
class Item(BaseModel):
    name: str
    price: float

@app.post("/predict")
def predict(item: Item):
    tax_price = item.price * 1.1
    return {
        "message": f"{item.name} costs {item.price} yen.",
        "tax_included": f"{tax_price:.0f} yen"
    }

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__=="__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
