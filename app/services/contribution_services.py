from sqlalchemy.orm import Session
from app.models.contribution import Contribution
from app.db.repository import ContributionRepository
from app.api.schemas import ContributionCreate, ContributionUpdate

class ContributionService:
    @staticmethod
    def get_contribution(contribution_id: int, db: Session):
        return ContributionRepository.get_contribution(db, contribution_id=contribution_id)

    @staticmethod
    def get_contributions(skip: int = 0, limit: int = 10, db: Session):
        return ContributionRepository.get_contributions(db, skip=skip, limit=limit)

    @staticmethod
    def create_contribution(contribution: ContributionCreate, db: Session):
        return ContributionRepository.create_contribution(db=db, contribution=contribution)

    @staticmethod
    def update_contribution(contribution_id: int, contribution: ContributionUpdate, db: Session):
        return ContributionRepository.update_contribution(db=db, contribution_id=contribution_id, contribution=contribution)

    @staticmethod
    def delete_contribution(contribution_id: int, db: Session):
        return ContributionRepository.delete_contribution(db=db, contribution_id=contribution_id)

    @staticmethod
    def get_contributions_by_language(language: str, db: Session):
        return ContributionRepository.get_contributions_by_language(db, language=language)
