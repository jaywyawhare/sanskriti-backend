from sqlalchemy.orm import Session
from app.models.user import User
from app.db.repository import UserRepository
from app.api.schemas import UserCreate, UserUpdate

class UserService:
    @staticmethod
    def get_user(user_id: int, db: Session):
        return UserRepository.get_user(db, user_id=user_id)

    @staticmethod
    def get_users(skip: int = 0, limit: int = 10, db: Session):
        return UserRepository.get_users(db, skip=skip, limit=limit)

    @staticmethod
    def create_user(user: UserCreate, db: Session):
        return UserRepository.create_user(db=db, user=user)

    @staticmethod
    def update_user(user_id: int, user: UserUpdate, db: Session):
        return UserRepository.update_user(db=db, user_id=user_id, user=user)

    @staticmethod
    def delete_user(user_id: int, db: Session):
        return UserRepository.delete_user(db=db, user_id=user_id)
