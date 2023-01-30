from fastapi import status, HTTPException, Response, Depends, APIRouter
from app.db.connection import get_db
from app.db import models
from app import schemas
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


@router.get("/")
def read_posts(database: Session = Depends(get_db)):
    return database.query(models.Post).all()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.PostResponse,
)
def create_posts(post: schemas.PostCreate, database: Session = Depends(get_db)):

    new_post = models.Post(**post.dict())
    database.add(new_post)
    database.commit()
    database.refresh(new_post)
    return new_post


@router.get("/{id}")
def get_post(id: int, database: Session = Depends(get_db)):

    post = database.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'failed to find post with id {id}',
        )

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, database: Session = Depends(get_db)):

    post = database.query(models.Post).filter(models.Post.id == id)

    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} does not exist')

    post.delete(synchronize_session=False)
    database.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update_post(
        id: int,
        updated_post: schemas.PostCreate,
        database: Session = Depends(get_db),
):
    post_query = database.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} does not exist')

    post_query.update(updated_post.dict(), synchronize_session=False)
    database.commit()
    return post_query.first()
