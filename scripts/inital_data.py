from sqlalchemy.orm import Session
from app.db.base_class import SessionLocal, engine
from app.models.user import User
from app.models.contribution import Contribution

def initialize_db():
    db = SessionLocal()
    User.metadata.create_all(bind=engine)
    Contribution.metadata.create_all(bind=engine)

if __name__ == "__main__":
    initialize_db()