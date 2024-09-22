from fastapi import APIRouter, Depends, status, HTTPException
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(prefix="/user", tags=["user"])

# Create
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read all users
@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Read one user
@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db_user.get_user(db, id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    return user

# Update
@router.put("/{id}")
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    response = db_user.update_user(db, id, request)
    
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    return "OK"

# Delete
@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    response = db_user.delete_user(db, id)

    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")

    return "OK"
