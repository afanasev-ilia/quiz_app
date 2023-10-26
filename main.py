import requests

from fastapi import FastAPI

from schema import Question_num

app = FastAPI()


@app.post('/questions')
def questions(item: Question_num):
    question_num = item.question_num
    response = requests.get(
        f'https://jservice.io/api/random?count={question_num}',
    )
    print(response.text)
