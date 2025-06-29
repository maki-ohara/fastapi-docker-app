# app/routers/predict.py
from fastapi import APIRouter
from schemas.predict import Item  # ← ここを変更
import logging

router = APIRouter()
logger = logging.getLogger("app_logger")

@router.post("/predict")
def predict(item: Item):
    tax_price = item.price * 1.1
    category = item.category.lower()

    if category == "food":
        prefix = "[FOOD]"
    elif category == "book":
        prefix = "[BOOK]"
    elif category == "clothing":
        prefix = "[CLOTHING]"
    else:
        prefix = "[OTHER]"

    logger.debug(f"カテゴリ: {category}, 税込価格: {tax_price}")
    return {
        "message": f"{prefix} {item.name} costs {item.price} yen.",
        "tax_included": f"{tax_price:.0f} yen"
    }
