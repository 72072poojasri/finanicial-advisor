from app.models import Project, User
from app.repositories import ProjectRepository
from app.schemas import ProjectCreate, ProjectUpdate


class ProjectService:
    def __init__(
        self,
        repository: ProjectRepository,
    ):
        self.repository = repository

    def create_project(
        self,
        request: ProjectCreate,
        current_user: User,
    ):
        project = Project(
            name=request.name,
            description=request.description,
            owner_id=current_user.id,
        )

        return self.repository.create(project)

    def get_projects(
        self,
        current_user: User,
    ):
        return self.repository.get_all_by_owner(
            current_user.id
        )

    def get_project(
        self,
        project_id: int,
    ):
        return self.repository.get_by_id(project_id)

    def update_project(
        self,
        project: Project,
        request: ProjectUpdate,
    ):
        if request.name is not None:
            project.name = request.name

        if request.description is not None:
            project.description = request.description

        return self.repository.update(project)

    def delete_project(
        self,
        project: Project,
    ):
        self.repository.delete(project)