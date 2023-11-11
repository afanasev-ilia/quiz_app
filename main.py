import aiohttp
from fastapi import FastAPI
from fastapi_sqlalchemy import db, DBSessionMiddleware
from sqlalchemy.sql import exists

from models import Question
from schemas import Question_num
from config import DATABASE_URL

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)


def get_last_question(model: Question = Question) -> Question:
    return db.session.query(model).order_by(model.id.desc()).first()


@app.post('/questions')
async def questions(item: Question_num):
    pass
    # last = get_last_question()
    # return last
    # question_num = item.question_num
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(
    #             f"https://jservice.io/api/random?count={question_num}"
    #     ) as resp:
    #         api_data = await resp.json()
    #         for model in api_data:
    #             while db.session.query(exists().where(model.question_id == model["id"])).scalar():
    #                 print(
    #                     f'id {model["id"]} with question: "{model["question"]}"'
    #                     f'is already exists in database!'
    #                 )
    #                 async with session.get(f'https://jservice.io/api/random') as api_res:
    #                     new_question = await api_res.json()
    #                     model = new_question[0]
    # return last.model if last else []
