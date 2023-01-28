from app.auth import AuthProvider, get_provider
from fastapi import status, Depends, APIRouter, HTTPException
from app import schemas


router = APIRouter(
    tags=['Users']
)


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
)
def register(user: schemas.User, auth: AuthProvider = Depends(get_provider)):
    if err := auth.register(user.email, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=err,
        )
    return {"email": user.email}


@router.post(
    "/signin",
    status_code=status.HTTP_200_OK,
)
def login(user: schemas.User, auth: AuthProvider = Depends(get_provider)):
    if err := auth.authenticate(user.email, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=err,
        )
