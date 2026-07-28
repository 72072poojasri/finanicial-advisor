from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import (
    get_current_user,
    get_task_service,
)
from app.models import User
from app.schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse,
)
from app.services import TaskService


# Project Task Routes
project_router = APIRouter(
    prefix="/api/projects",
    tags=["Tasks"],
)


@project_router.post(
    "/{project_id}/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    project_id: int,
    request: TaskCreate,
    current_user: User = Depends(get_current_user),
    service: TaskService = Depends(get_task_service),
):
    task = service.create_task(request, project_id, current_user)

    if task is None:
        raise HTTPException(404, "Project not found")

    if task is False:
        raise HTTPException(403, "Access denied")

    return task


@project_router.get(
    "/{project_id}/tasks",
    response_model=list[TaskResponse],
)
def get_tasks(
    project_id: int,
    current_user: User = Depends(get_current_user),
    service: TaskService = Depends(get_task_service),
):
    tasks = service.get_tasks(project_id, current_user)

    if tasks is None:
        raise HTTPException(404, "Project not found")

    if tasks is False:
        raise HTTPException(403, "Access denied")

    return tasks


# Individual Task Routes
router = APIRouter(
    prefix="/api/tasks",
    tags=["Tasks"],
)


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
def get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    service: TaskService = Depends(get_task_service),
):
    task = service.get_task(task_id, current_user)

    if task is None:
        raise HTTPException(404, "Task not found")

    if task is False:
        raise HTTPException(403, "Access denied")

    return task


@router.put(
    "/{task_id}",
    response_model=TaskResponse,
)
def update_task(
    task_id: int,
    request: TaskUpdate,
    current_user: User = Depends(get_current_user),
    service: TaskService = Depends(get_task_service),
):
    task = service.get_task(task_id, current_user)

    if task is None:
        raise HTTPException(404, "Task not found")

    if task is False:
        raise HTTPException(403, "Access denied")

    return service.update_task(task, request)


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    service: TaskService = Depends(get_task_service),
):
    task = service.get_task(task_id, current_user)

    if task is None:
        raise HTTPException(404, "Task not found")

    if task is False:
        raise HTTPException(403, "Access denied")

    service.delete_task(task)