from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from .connection import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    accident_title = Column(String, nullable=False)
    description_emotions = Column(String, nullable=False)
    description_thoughts = Column(String, nullable=False)
    body_reaction = Column(String, nullable=False)
    rational_thoughts = Column(String, nullable=False)
    rational_actions = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
