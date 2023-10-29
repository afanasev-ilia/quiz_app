import aiohttp
from fastapi import FastAPI
from fastapi_asyncalchemy import db
from sqlalchemy.sql import exists

from schema import Question_num

app = FastAPI()

def get_last_question(model: ModelQuestion = ModelQuestion) -> ModelQuestion:
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
            for model in api_data:
                while db.session.query(exists().where(model.question_id == model["id"])).scalar():
                    print(
                        f'id {model["id"]} with question: "{model["question"]}" '
                        f'is already exists in database!'
                    )
                    async with session.get(f'https://jservice.io/api/random') as api_res:
                        new_question = await api_res.json()
                        model = new_question[0]
    return last.model if last else []