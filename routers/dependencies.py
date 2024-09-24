from fastapi import APIRouter, Depends
from fastapi.requests import Request
from typing import Optional

router = APIRouter(
    prefix="/dependencies",
    tags=["dependencies"]
)

def convert_headers(request: Request, seperator: str = "--"):
    out_headers = []
    for key, value in request.headers.items():
        out_headers.append(f"{key} {seperator} {value}")
    return out_headers

@router.get('')
def get_items(seperator: str = "--", headers = Depends(convert_headers)):
    return {
        "items": ['a', 'b', 'c'],
        "headers": headers
    }