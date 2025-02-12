from sqlalchemy import create_engine
from model.models import Base
from sqlalchemy.orm import Session

def get_db_engine():
    return create_engine('sqlite:///accounting_assistant.db')

def init_db():
    db_engine=get_db_engine()
    Base.metadata.create_all(db_engine, checkfirst=True)
