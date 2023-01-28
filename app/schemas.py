from datetime import datetime

from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    accident_title: str
    description_emotions: str
    description_thoughts: str
    body_reaction: str
    rational_thoughts: str
    rational_actions: str
    published : bool = True


class PostCreate(PostBase):
    pass


class PostResponse(BaseModel):
    accident_title: str
    description_emotions: str
    description_thoughts: str
    body_reaction: str
    rational_thoughts: str
    rational_actions: str
    published: bool
    created_at: datetime

    class Config:
        orm_mode = True


class User(BaseModel):
    email: EmailStr
    password: str


class SignUpResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
