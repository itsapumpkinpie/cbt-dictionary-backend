from fastapi import FastAPI
from fastapi.params import Body
import uvicorn

app = FastAPI()


@app.get("/posts")
def read_posts():
    return {"massage": "our posts"}

@app.get("/posts/{post_id}")
def get_one_post(post_id: int):
    return {"post_id": post_id}


@app.post("/createpost")
def create_post(postData: dict = Body(...)):
    print(postData)
    return {"new_post": f"title: {postData['title']} content:  {postData['content']}"}


@app.put("/update_post")
def update_post():
    return {"massage": "post the post data has been updated"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
