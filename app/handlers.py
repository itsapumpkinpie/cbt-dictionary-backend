from fastapi import APIRouter, Body, Depends

from app.forms import UserLoginForm
from app.models import connect_db


router = APIRouter()

@router.get('/login', name='user:login')
def login(user_form: UserLoginForm = Body(..., embed=True), database=()):
    return {'status': 'OK'}