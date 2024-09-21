from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

# Hello world example
@app.get('/hello')
def index():
    return {
        'message': "Hello World"
    }

# Order is important here.  If this comes after the next one it will think
# we are trying to call the other one with "all" as the ID
@app.get('/blog/all')
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {
        'message': f"All {page_size} blogs on page {page} provided"
    }

@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, user_name: Optional[str] = None):
    return {
        'message': f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {user_name}"
    }

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {
        'message': f"Blog type {type}"
    }

# Example using path parameters
@app.get('/blog/{id}')
def get_blog(id: int): # Make sure the ID is a valid integer
    return {
        'message': f"Blog with id {id}"
    }