from fastapi import FastAPI

from app.controllers import (
    auth_router,
    user_router,
    project_router,
    project_task_router,
    task_router,
)

from app.core.exception_handler import register_exception_handlers
from app.database.init_db import init_db


app = FastAPI(
    title="Financial Advisor Process Management API",
    version="1.0.0",
)


register_exception_handlers(app)


@app.on_event("startup")
def startup():
    init_db()


# Authentication
app.include_router(auth_router)

# User
app.include_router(user_router)

# Project CRUD
app.include_router(project_router)

# Project -> Task Routes
app.include_router(project_task_router)

# Individual Task Routes
app.include_router(task_router)


@app.get("/")
def root():
    return {
        "message": "Financial Advisor Process Management API is running successfully"
    }