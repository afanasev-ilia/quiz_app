from datetime import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    question_id: int
    question: str
    answer: str
    created_at: datetime


class Question_num(BaseModel):
    question_num: int
