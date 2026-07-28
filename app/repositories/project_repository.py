from sqlalchemy.orm import Session

from app.models import Project


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, project: Project):
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def get_by_id(self, project_id: int):
        return (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    def get_all_by_owner(self, owner_id: int):
        return (
            self.db.query(Project)
            .filter(Project.owner_id == owner_id)
            .all()
        )

    def update(self, project: Project):
        self.db.commit()
        self.db.refresh(project)
        return project

    def delete(self, project: Project):
        self.db.delete(project)
        self.db.commit()