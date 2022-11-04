from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from .сonnection import Base


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True, nullable=False)
    accident_title = Column(String, nullable=False)
    description_emotions = Column(String)
    description_thoughts = Column(String)
    body_reaction = Column(String)
    rational_thoughts = Column(String)
    rational_actions = Column(String)
    published = Column(Boolean, server_default="TRUE")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
