from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class Contribution(Base):
    __tablename__ = "contributions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    language = Column(String, index=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    user = relationship("User", back_populates="contributions")
