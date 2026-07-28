from app.models import Task, User
from app.repositories import (
    TaskRepository,
    ProjectRepository,
)
from app.schemas import (
    TaskCreate,
    TaskUpdate,
)


class TaskService:
    def __init__(
        self,
        task_repository: TaskRepository,
        project_repository: ProjectRepository,
    ):
        self.repository = task_repository
        self.project_repository = project_repository

    def create_task(
        self,
        request: TaskCreate,
        project_id: int,
        current_user: User,
    ):
        project = self.project_repository.get_by_id(project_id)

        if not project:
            return None

        if project.owner_id != current_user.id:
            return False

        task = Task(
            title=request.title,
            description=request.description,
            status=request.status,
            priority=request.priority,
            project_id=project_id,
        )

        return self.repository.create(task)

    def get_tasks(
        self,
        project_id: int,
        current_user: User,
    ):
        project = self.project_repository.get_by_id(project_id)

        if not project:
            return None

        if project.owner_id != current_user.id:
            return False

        return self.repository.get_all_by_project(project_id)

    def get_task(
        self,
        task_id: int,
        current_user: User,
    ):
        task = self.repository.get_by_id(task_id)

        if not task:
            return None

        project = self.project_repository.get_by_id(task.project_id)

        if project.owner_id != current_user.id:
            return False

        return task

    def update_task(
        self,
        task: Task,
        request: TaskUpdate,
    ):
        if request.title is not None:
            task.title = request.title

        if request.description is not None:
            task.description = request.description

        if request.status is not None:
            task.status = request.status

        if request.priority is not None:
            task.priority = request.priority

        return self.repository.update(task)

    def delete_task(
        self,
        task: Task,
    ):
        self.repository.delete(task)