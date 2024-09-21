from fastapi import status, Response, APIRouter
from enum import Enum
from typing import Optional

router = APIRouter(prefix="/blog", tags=['blog'])

# Order is important here.  If this comes after the next one it will think
# we are trying to call the other one with "all" as the ID
@router.get(
    '/all', 
    summary="Retrieve all blogs",
    description="This API call simulates fetching all blogs.",
    response_description= "The list of available blogs"
) 
def get_all_blogs(
    page=1, 
    page_size: Optional[int] = None
):
    return {
        'message': f"All {page_size} blogs on page {page} provided"
    }

@router.get(
    '/{id}/comments/{comment_id}', 
    tags=['comment']
)
def get_comment(id: int, comment_id: int, valid: bool = True, user_name: Optional[str] = None):
    '''
    Simulates retrieving a comment of a blog
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **user_name** optional query parameter
    '''
    return {
        'message': f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {user_name}"
    }

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get(
    '/type/{type}', 
    tags=['blog']
)
def get_blog_type(type: BlogType):
    return {
        'message': f"Blog type {type}"
    }

# Example using path parameters
@router.get(
    '/{id}', 
    status_code=status.HTTP_200_OK 
)
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