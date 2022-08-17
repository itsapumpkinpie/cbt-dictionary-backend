from pydantic import BaseModel

class UserLoginForm(BaseModel):
    email: str
    password: str