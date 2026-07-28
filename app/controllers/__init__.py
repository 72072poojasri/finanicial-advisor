from .auth_controller import router as auth_router
from .user_controller import router as user_router
from .project_controller import router as project_router
from .task_controller import (
    router as task_router,
    project_router as project_task_router,
)