from fastapi import FastAPI, status, Response
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
@app.get('/blog/all', tags=['blog']) # Tags organize the swagger docs
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {
        'message': f"All {page_size} blogs on page {page} provided"
    }

@app.get('/blog/{id}/comments/{comment_id}', tags=['blog', 'comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, user_name: Optional[str] = None):
    return {
        'message': f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {user_name}"
    }

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {
        'message': f"Blog type {type}"
    }

# Example using path parameters
@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response): # Make sure the ID is a valid integer
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            'error': f"Blog {id} not found"
        }
    else:
        response.status_code = status.HTTP_200_OK
        return {
            'message': f"Blog with id {id}"
        }