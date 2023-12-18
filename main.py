import aiohttp

from fastapi import FastAPI
from fastapi_sqlalchemy import db, DBSessionMiddleware
from sqlalchemy.sql import exists

from models import Question
from schemas import Question_num
from config import DATABASE_URL

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)


def is_question_id_exists(question: dict, model: Question = Question) -> bool:
    return db.session.query(
        exists().where(model.question_id == question['id'])
    ).scalar()


def get_last_question(model: Question = Question) -> Question:
    return db.session.query(model).order_by(model.id.desc()).first()


@app.post('/questions')
async def questions(item: Question_num):
    last = get_last_question()
    question_num = item.question_num
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f"https://jservice.io/api/random?count={question_num}"
        ) as resp:
            api_data = await resp.json()
            for q in api_data:
                while is_question_id_exists(q):
                    print(
                        f'id {q["id"]} with question: "{q["question"]}" '
                        f'is already exists in database!'
                    )
                    async with session.get(
                        f"https://jservice.io/api/random",
                    ) as api_res:
                        new_question = await api_res.json()
                        q = new_question[0]

                db_question = Question(
                    question_id=q["id"],
                    question=q["question"],
                    answer=q["answer"],
                    created_at=q["created_at"],
                )
                db.session.add(db_question)
            db.session.commit()

    return last.question if last else []
