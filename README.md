# quiz_app

## Описание

Приложение с вопросами для викторин

## Технологии

Python 3.9 FastAPI 0.104.1

## Запуск проекта в dev-режиме

Клонируем репозиторий и переходим в него в командной строке:

```bash
git clone https://github.com/afanasev-ilia/quiz_app
```

```bash
cd quiz_app
```

Устанавливаем и активируем виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

Устанавливаем зависимости из файла requirements.txt

```bash
pip install -r requirements.txt
``` 

Запускаем сервер в режиме разработки:

```bash
uvicorn main:app --reload
```
