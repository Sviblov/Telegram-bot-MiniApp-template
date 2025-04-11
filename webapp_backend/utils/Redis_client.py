import redis.asyncio as redis
from typing import Optional
import json

class RedisClient:

    def __init__(self, host: str, port: int, password:str, bot_token: str, db: int=0):
    
        self.redis = redis.from_url(f"redis://:{password}@{host}:{port}/{db}", decode_responses=True)
        self.bot_id = bot_token.split(":")[0]


    async def setData(self, user_id: str, value: str):
        key= f"fsm:{self.bot_id}:{user_id}:{user_id}:default:data"
        value_json = json.dumps(value)  # Сериализация словаря в JSON
        await self.redis.set(key, value_json)

    async def getData(self, user_id: str):
        key= f"fsm:{self.bot_id}:{user_id}:{user_id}:default:data"
        data_json = await self.redis.get(key)
        data=json.loads(data_json)
        return data

    async def close(self):
        await self.redis.close()

    async def setToken(self, user_id: str, token: str):
        key = f"fsm:{self.bot_id}:{user_id}:{user_id}:default:token"

        await self.redis.set(key, token)
    
    async def getToken(self, user_id: str):
        key = f"fsm:{self.bot_id}:{user_id}:{user_id}:default:token"
        token = await self.redis.get(key)
        return token