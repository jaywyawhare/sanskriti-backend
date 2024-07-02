from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from app.core.security import create_access_token, verify_password, hash_password
from app.models.user import User
from app.db.repository import UserRepository
from app.core.config import settings

router = APIRouter()

class UserLogin(BaseModel):
    email: str
    password: str

class UserRegister(BaseModel):
    email: str
    password: str

@router.post("/login", response_model=Token)
def login(user_login: UserLogin, db: Session = Depends(UserRepository.get_db)):
    user = UserRepository.get_user_by_email(db, user_login.email)
    if not user or not verify_password(user_login.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token}

@router.post("/register", response_model=Token)
def register(user_register: UserRegister, db: Session = Depends(UserRepository.get_db)):
    user = UserRepository.get_user_by_email(db, user_register.email)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    hashed_password = hash_password(user_register.password)
    new_user = UserRepository.create_user(db, User(email=user_register.email, password_hash=hashed_password))
    access_token = create_access_token({"sub": new_user.email})
    return {"access_token": access_token}

@router.get("/logout")
def logout():
    return {"message": "Logged out"}

@router.get("/me", response_model=User)
def me(current_user: User = Depends(UserRepository.get_current_user)):
    return current_user

@router.get("/admin")
def admin(current_user: User = Depends(UserRepository.get_current_user)):
    if not current_user.role == "admin":
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "You are allowed to see this message"}
