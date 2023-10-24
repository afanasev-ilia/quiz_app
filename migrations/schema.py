from pydantic import BaseModel


class Table(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True
