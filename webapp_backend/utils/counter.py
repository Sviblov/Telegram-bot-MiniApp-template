from pydantic import BaseModel


class Counter(BaseModel):
    counter: int
    