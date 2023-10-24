from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_index():
    return 'index page'
