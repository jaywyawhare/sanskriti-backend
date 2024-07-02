from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class ContributionBase(BaseModel):
    language: str
    question: str
    answer: str

class ContributionCreate(ContributionBase):
    pass

class ContributionUpdate(ContributionBase):
    pass
