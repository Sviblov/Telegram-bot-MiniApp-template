import logging
import uvicorn
import betterlogging as bl
import fastapi
# from aiogram import Bot
from fastapi import FastAPI, Depends
from starlette.responses import JSONResponse 
from webapp_backend.config import load_config
from fastapi.middleware.cors import CORSMiddleware

import hmac
import hashlib
from urllib.parse import unquote

from fastapi.security import HTTPBasic, HTTPBasicCredentials

from infrastructure.database.setup import create_engine
from infrastructure.database.setup import create_session_pool
from infrastructure.database.repo.requests import RequestsRepo

from sqlalchemy.ext.asyncio import AsyncSession

#from tgbot.config import load_config, Config

app = FastAPI()

allowed_origins = [
    "http://localhost:3000",  # Allow frontend origin
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # List of allowed origins
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


@app.post("/api")
async def webhook_endpoint(request: fastapi.Request):
    return JSONResponse(status_code=200, content={"status": "ok"})

@app.get("/validation")
async def webhook_validation(request: fastapi.Request, repo: AsyncSession = Depends(get_repo)):
    
    message = await repo.interface.get_MessageText('welcome_not_admin')
    
    return JSONResponse(status_code=200, content={"isValid": True})

# @app.get("/validate")
# async def getVerification(request: fastapi.Request):

#     Authorization = request.headers.get("Authorization")
#     initData = request.query_params.get("initData")
#     hash = request.query_params.get("hash")
#     token = config.tg_bot.token
#     dataValidation = validate(hash, initData, token)
#     print(request.query_params)
#     return JSONResponse(status_code=200, content={"status": "validated"})


# def validate(hash_str, init_data, token, c_str="WebAppData"):
#     """
#     Validates the data received from the Telegram web app, using the
#     method documented here: 
#     https://core.telegram.org/bots/webapps#validating-data-received-via-the-web-app

#     hash_str - the has string passed by the webapp
#     init_data - the query string passed by the webapp
#     token - Telegram bot's token
#     c_str - constant string (default = "WebAppData")
#     """

#     init_data = sorted([ chunk.split("=") 
#           for chunk in unquote(init_data).split("&") 
#             if chunk[:len("hash=")]!="hash="],
#         key=lambda x: x[0])
#     init_data = "\n".join([f"{rec[0]}={rec[1]}" for rec in init_data])

#     secret_key = hmac.new(c_str.encode(), token.encode(),
#         hashlib.sha256 ).digest()
#     data_check = hmac.new( secret_key, init_data.encode(),
#         hashlib.sha256)

#     return data_check.hexdigest() == hash_str