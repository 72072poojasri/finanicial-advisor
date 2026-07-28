from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories import ProjectRepository
from app.services import ProjectService


def get_project_service(
    db: Session = Depends(get_db),
):
    repository = ProjectRepository(db)
    return ProjectService(repository)