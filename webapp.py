import logging

import betterlogging as bl
import fastapi
# from aiogram import Bot

from fastapi import FastAPI
from starlette.responses import JSONResponse 
from webapp_backend.config import load_config
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import parse_qsl
from hashlib import sha256
import hmac

from fastapi.security import HTTPBasic
from webapp_backend.utils.telegram_validation import validate_telegram_init_data, InitData
from infrastructure.database.setup import create_engine
from infrastructure.database.setup import create_session_pool
from infrastructure.database.repo.requests import RequestsRepo
from fastapi import FastAPI, HTTPException
from webapp_backend.utils.counter import Counter    
#from tgbot.config import load_config, Config
import redis.asyncio as redis
from webapp_backend.utils.Redis_client import RedisClient

#     setup_logging()
app = FastAPI()

allowed_origins = [
    "https://localhost:4000",  # Allow frontend origin
    "https://127.0.0.1:4000",
    "http://10.0.0.137:4000",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=allowed_origins,  # List of allowed origins
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Allow cookies
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


log_level = logging.INFO
bl.basic_colorized_config(level=log_level)
log = logging.getLogger('backend')

config = load_config(".env")

security = HTTPBasic()



# config: Config = load_config()
db_engine=create_engine(config.db)
session_pool = create_session_pool(db_engine)
# Dependency to get DB session
async def get_repo():
    async with session_pool() as session:
        yield RequestsRepo(session)
      
# bot = Bot(token=config.tg_bot.token)

BOT_TOKEN = config.tg_bot.token


redisClient=RedisClient(config.redis.redis_host, config.redis.redis_port,config.redis.redis_pass, config.tg_bot.token)



@app.get("/api")
async def webhook_endpoint(request: fastapi.Request):
    return JSONResponse(status_code=200, content={"status": "ok"})

@app.post("/validate")
async def validate(data: InitData):

    is_valid = validate_telegram_init_data(data.init_data, BOT_TOKEN)
    return {"valid": is_valid}


@app.get("/counter/{user_id}")
async def get_counter(user_id: int):
    """
    Возвращает текущее значение счетчика.
    """
    userData = await redisClient.getData(user_id)
    return userData

@app.post("/counter")
async def update_counter(data: dict):
    """
    Обновляет значение счетчика.
    """
    user_id = data.get("user_id")
    counter_value = data.get("counter")
    if user_id is None or counter_value is None:
        raise HTTPException(status_code=400, detail="user_id and counter are required")
   
    await redisClient.setData(user_id, {"counter": counter_value})
    return {"status": "success"}