from typing import Optional
from fastapi import FastAPI, status, HTTPException, Response, Depends
import uvicorn
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .db import models
from .db.сonnection import engine, get_db


class Post(BaseModel):
    accident_title: Optional[str]
    description_emotions: Optional[str]
    description_thoughts: Optional[str]
    body_reaction: Optional[str]
    rational_thoughts: Optional[str]
    rational_actions: Optional[str]
    published: bool = True


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/posts")
def read_posts(database: Session = Depends(get_db)):
    posts = database.query(models.Post).all()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, database: Session = Depends(get_db)):
    new_post = models.Post(accident_title=post.accident_title,
                           description_emotions=post.description_emotions,
                           description_thoughts=post.description_thoughts,
                           body_reaction=post.body_reaction,
                           rational_thoughts=post.rational_thoughts,
                           rational_actions=post.rational_actions,
                           published=post.published)

    # new_post = models.Post(**post.dict())

    database.add(new_post)
    database.commit()
    database.refresh(new_post)
    return {"post_data": new_post}


@app.get("/posts/{post_id}")
def get_post(post_id: int, database: Session = Depends(get_db)):
    post = database.query(models.Post).filter(models.Post.post_id == post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {post_id} was not found')

    return {"data of one post": post}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, database: Session = Depends(get_db)):
    post = database.query(models.Post).filter(models.Post.post_id == post_id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {post_id} does not exist')

    post.delete(synchronize_session=False)
    database.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{post_id}")
def update_post(post_id: int, updated_post: Post, database: Session = Depends(get_db)):
    post_query = database.query(models.Post).filter(models.Post.post_id == post_id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {post_id} does not exist')

    post_query.update(updated_post.dict(), synchronize_session=False)
    database.commit()
    return {'data': post_query.first()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
