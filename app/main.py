from fastapi import FastAPI
import uvicorn
from app.db import models
from app.db.connection import engine
from app.routers import post, user


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(post.router)

app.include_router(user.router)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
