from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.contribution import Contribution
from app.db.repository import ContributionRepository
from app.api.schemas import ContributionCreate, ContributionUpdate

router = APIRouter()

@router.get("/", response_model=List[Contribution])
def read_contributions(skip: int = 0, limit: int = 10, db: Session = Depends(ContributionRepository.get_db)):
    contributions = ContributionRepository.get_contributions(db, skip=skip, limit=limit)
    return contributions

@router.get("/{contribution_id}", response_model=Contribution)
def read_contribution(contribution_id: int, db: Session = Depends(ContributionRepository.get_db)):
    db_contribution = ContributionRepository.get_contribution(db, contribution_id=contribution_id)
    if db_contribution is None:
        raise HTTPException(status_code=404, detail="Contribution not found")
    return db_contribution

@router.post("/", response_model=Contribution)
def create_contribution(contribution: ContributionCreate, db: Session = Depends(ContributionRepository.get_db)):
    return ContributionRepository.create_contribution(db=db, contribution=contribution)

@router.put("/{contribution_id}", response_model=Contribution)
def update_contribution(contribution_id: int, contribution: ContributionUpdate, db: Session = Depends(ContributionRepository.get_db)):
    db_contribution = ContributionRepository.update_contribution(db=db, contribution_id=contribution_id, contribution=contribution)
    if db_contribution is None:
        raise HTTPException(status_code=404, detail="Contribution not found")
    return db_contribution

@router.delete("/{contribution_id}", response_model=Contribution)
def delete_contribution(contribution_id: int, db: Session = Depends(ContributionRepository.get_db)):
    db_contribution = ContributionRepository.delete_contribution(db=db, contribution_id=contribution_id)
    if db_contribution is None:
        raise HTTPException(status_code=404, detail="Contribution not found")
    return db_contribution

@router.get("/language/{language}", response_model=List[Contribution])
def read_contributions_by_language(language: str, db: Session = Depends(ContributionRepository.get_db)):
    contributions = ContributionRepository.get_contributions_by_language(db, language=language)
    return contributions
