import logging

import betterlogging as bl
import fastapi
# from aiogram import Bot

from fastapi import FastAPI,Header, Depends
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
import json
import jwt
from datetime import datetime, timedelta, timezone



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
secretKey = config.misc.secret_key


# config: Config = load_config()
db_engine=create_engine(config.db)
session_pool = create_session_pool(db_engine)
# Dependency to get DB session
async def get_repo():
    async with session_pool() as session:
        yield RequestsRepo(session)


redisClient=RedisClient(config.redis.redis_host, config.redis.redis_port,config.redis.redis_pass, config.tg_bot.token)

def verify_token(token: str = Header(...)):
    try:
        # Декодируем токен
        payload = jwt.decode(token, secretKey, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
  
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")



@app.get("/api")
async def webhook_endpoint(request: fastapi.Request):

    return JSONResponse(status_code=200, content={"status": "ok"})

@app.post("/validate")
async def validate(data: InitData):

    is_valid = validate_telegram_init_data(data.init_data, config.tg_bot.token)
    if not is_valid:
        log.error("Invalid Telegram data")
        raise HTTPException(status_code=400, detail="Invalid Telegram data")

    try:
        init_data_dict = dict(parse_qsl(data.init_data, keep_blank_values=True))
        user_data=json.loads(init_data_dict["user"])
    except json.JSONDecodeError:
        log.error("Invalid init_data format")
        raise HTTPException(status_code=400, detail="Invalid init_data format")

    payload = {
        "user_id": user_data["id"],  # ID пользователя
        "exp": datetime.now(timezone.utc)+ timedelta(hours=1),  # Время истечения токена
    }
    token = jwt.encode(payload, secretKey, algorithm="HS256")

    return {"valid": is_valid,"token": token}


@app.get("/counter/{user_id}")
async def get_counter(user_id: int, payload: dict = Depends(verify_token), repo: RequestsRepo = Depends(get_repo)):
    """
    Возвращает текущее значение счетчика.
    """
    userData = await repo.users.get_user(user_id)
    log.info(f"User from DB: {userData.full_name} ")
    
    if payload["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Access denied")
   

    userData = await redisClient.getData(user_id)
    return userData

@app.post("/counter")
async def update_counter(request: Counter, payload: dict = Depends(verify_token)):
    """
    Обновляет значение счетчика.
    """
    if payload["user_id"] != request.user_id:
        raise HTTPException(status_code=403, detail="Access denied")
   
    if request.user_id is None or request.counter is None:
        raise HTTPException(status_code=400, detail="user_id and counter are required")
   
    await redisClient.setData(request.user_id, {"counter": request.counter})
    return {"status": "success"}