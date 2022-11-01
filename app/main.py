from fastapi import FastAPI, status, HTTPException, Response
import uvicorn
from pydantic import BaseModel
from random import randrange


class Post(BaseModel):
    post_id: int | None = None
    title: str | None = None
    emotions: str | None = None
    thoughts: str | None = None
    body_reaction: str | None = None
    rational_thoughts: str | None
    rational_actions: str | None
    published: bool = True


app = FastAPI()


my_future_database_posts = [
    {"post_id": 1,
     "title": 6,
     "emotions": "some emotions",
     "thoughts": "some thoughts",
     "body_reaction": "some body reaction",
     "rational_thoughts": "some rational thoughts",
     "rational_actions": "some rational actions",
     "published": True
     }
]


def find_one_post(post_id):
    for post in my_future_database_posts:
        if post["post_id"] == post_id:
            return post


def find_index_post(post_id):
    for index, post in enumerate(my_future_database_posts):
        if post["post_id"] == post_id:
            return index


@app.get("/posts")
def get_posts():
    return {"data of all posts": my_future_database_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):

    post_dict = post.dict()
    post_dict["post_id"] = randrange(0, 10000)

    my_future_database_posts.append(post_dict)
    return {"post_data": post_dict}


@app.get("/posts/{post_id}")
def get_post(post_id: int):

    post = find_one_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {post_id} was not found')

    return {"data of one post": post}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):

    index = find_index_post(post_id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {post_id} does not exist')

    my_future_database_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):

    index = find_index_post(post_id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {post_id} does not exist')

    post_dict = post.dict()
    post_dict["post_id"] = post_id
    my_future_database_posts[index] = post_dict
    return {"data": post_dict}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
