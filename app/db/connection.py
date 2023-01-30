import time
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DEFAULT_POSTGRES_HOST = "0.0.0.0"
POSTGRES_HOST = os.environ.get("POSTGRES_HOST") or DEFAULT_POSTGRES_HOST
POSTGRES_URL = f"postgresql://admin:password@{POSTGRES_HOST}/cbt"
CONN_RETRIES = 10

engine = create_engine(POSTGRES_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
