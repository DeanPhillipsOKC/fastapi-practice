from fastapi import APIRouter, Query
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

@router.post('/new/{id}/comment')
def create_comment(
    blog: BlogModel, 
    id: int, 
    comment_id: int = Query(None, title="ID of the comment", description="Some description for comment_id", alias="commentId", deprecated=True)
):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id
    }