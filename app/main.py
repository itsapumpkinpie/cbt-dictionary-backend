from fastapi import FastAPI
from fastapi.params import Body
import uvicorn
from pydantic import BaseModel


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



@app.get("/posts")
def read_posts(post: dict = Body()):
    return {"read all posts": post}

@app.get("/posts/{post_id}")
def get_one_post(post_id: int):
    return {"post_id": post_id}


@app.post("/posts")
def create_post(post: Post):
    print(post.post_id, post.published)
    print(post.dict())
    return {"post_data": post}


@app.put("/posts/{post_id}")
def update_post():
    return {"massage": "post the post data has been updated"}

@app.delete("/posts/{post_id}")
def delete_post():
    return {"post was successfully deleted"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
