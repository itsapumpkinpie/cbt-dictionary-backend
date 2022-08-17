from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def connect_db():
    engine = create_engine('', connect_args={})
    session = Session(bind=engine.connect())
    return session
