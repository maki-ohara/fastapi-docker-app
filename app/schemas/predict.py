# app/schemas/predict.py

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    category: str
