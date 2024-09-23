from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routers import blog_get, blog_post, user, article, product, file
from auth import authentication
from pydantic import BaseModel
from db import models
from db.database import engine
from exceptions import StoryException
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles # Requires aiofile
import time

load_dotenv()

app = FastAPI()
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(article.router)
app.include_router(product.router)

# Hello world example
@app.get('/hello')
def index():
    return {
        'message': "Hello World"
    }

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={
            'detail': exc.name
        }
    )

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: HTTPException):
#     return PlainTextResponse(str(exc), status_code=400)

models.Base.metadata.create_all(bind=engine)

@app.middleware("http")
async def add_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers['duration'] = str(duration)
    return response

app.mount('/files', StaticFiles(directory='files'), name='files')