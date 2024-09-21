from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/blog", tags=['blog'])

class BlogModel(BaseModel):
    title: str
    content: str
    num_comments: int
    published: Optional[bool]

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }