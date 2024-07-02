from sqlalchemy.orm import Session
from app.models.user import User
from app.models.contribution import Contribution
from app.db.session import SessionLocal

class UserRepository:
    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 10):
        return db.query(User).offset(skip).limit(limit).all()

    @staticmethod
    def create_user(db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def update_user(db: Session, user_id: int, user: User):
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            for key, value in user.dict(exclude_unset=True).items():
                setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(db: Session, user_id: int):
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
        return db_user

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

class ContributionRepository:
    @staticmethod
    def get_contribution(db: Session, contribution_id: int):
        return db.query(Contribution).filter(Contribution.id == contribution_id).first()

    @staticmethod
    def get_contributions(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Contribution).offset(skip).limit(limit).all()

    @staticmethod
    def create_contribution(db: Session, contribution: Contribution):
        db.add(contribution)
        db.commit()
        db.refresh(contribution)
        return contribution

    @staticmethod
    def update_contribution(db: Session, contribution_id: int, contribution: Contribution):
        db_contribution = db.query(Contribution).filter(Contribution.id == contribution_id).first()
        if db_contribution:
            for key, value in contribution.dict(exclude_unset=True).items():
                setattr(db_contribution, key, value)
            db.commit()
            db.refresh(db_contribution)
        return db_contribution

    @staticmethod
    def delete_contribution(db: Session, contribution_id: int):
        db_contribution = db.query(Contribution).filter(Contribution.id == contribution_id).first()
        if db_contribution:
            db.delete(db_contribution)
            db.commit()
        return db_contribution

    @staticmethod
    def get_contributions_by_language(db: Session, language: str):
        return db.query(Contribution).filter(Contribution.language == language).all()
