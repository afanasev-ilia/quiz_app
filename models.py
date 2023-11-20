from datetime import datetime

from sqlalchemy import Column, Integer, MetaData, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()

Base = declarative_base()


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer)
    question = Column(String)
    answer = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
