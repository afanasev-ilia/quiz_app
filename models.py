from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP

metadata = MetaData()


question = Table(
    'question',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('question_id', Integer),
    Column('question', String),
    Column('answer', String),
    Column('created_at', TIMESTAMP, default=datetime.utcnow),
)
