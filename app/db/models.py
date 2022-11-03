from sqlalchemy import Column, Integer, TEXT, String, Boolean
from .сonnection import Base


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True, nullable=False)
    accident_title = Column(String, nullable=False)
    description_emotions = Column(TEXT)
    description_thoughts = Column(TEXT)
    body_reaction = Column(TEXT)
    rational_thoughts = Column(TEXT)
    rational_actions = Column(TEXT)
    published = Column(Boolean, default=True)


