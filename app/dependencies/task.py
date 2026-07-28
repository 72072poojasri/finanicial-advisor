from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories import (
    TaskRepository,
    ProjectRepository,
)
from app.services import TaskService


def get_task_service(
    db: Session = Depends(get_db),
):
    task_repository = TaskRepository(db)
    project_repository = ProjectRepository(db)

    return TaskService(
        task_repository,
        project_repository,
    )