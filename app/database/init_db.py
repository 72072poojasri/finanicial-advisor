from app.database.database import Base, engine

# Import all models so SQLAlchemy registers them
from app.models import Project, Task, User  # noqa: F401


def init_db():
    Base.metadata.create_all(bind=engine)