from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP


from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
# metadata = MetaData()

Base = declarative_base()


class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# question = Table(
#     'question',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('question_id', Integer),
#     Column('question', String),
#     Column('answer', String),
#     Column('created_at', TIMESTAMP, default=datetime.utcnow),
# )
