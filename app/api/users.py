from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.user import User
from app.db.repository import UserRepository
from app.api.schemas import UserCreate, UserUpdate

router = APIRouter()

@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(UserRepository.get_db)):
    users = UserRepository.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(UserRepository.get_db)):
    db_user = UserRepository.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(UserRepository.get_db)):
    return UserRepository.create_user(db=db, user=user)

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(UserRepository.get_db)):
    db_user = UserRepository.update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(UserRepository.get_db)):
    db_user = UserRepository.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
