from pydantic import BaseModel

class Counter(BaseModel):
    counter: int
    user_id: int