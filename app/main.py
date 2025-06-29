# app/main.py

import os
import logging
from fastapi import FastAPI

from logger import setup_logger
from routers import items, predict  # ← 分けたルーターをインポート

app = FastAPI()

# ログ設定
logger = setup_logger()
logger.info("FastAPI アプリ起動完了")

@app.get("/")
def read_root():
    env = os.getenv("APP_ENV", "default")
    debug = os.getenv("DEBUG", "false")
    return {
        "Hello": "World (復活！)",
        "env": env,
        "debug_mode": debug
    }

# 分離したルーターを登録
app.include_router(items.router)
app.include_router(predict.router)
