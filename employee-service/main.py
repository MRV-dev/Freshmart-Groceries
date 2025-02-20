from fastapi import FastAPI
from database.db import Base, engine
from routes import employee

# Create tables (if not using Alembic for migrations)
Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI(title="Employee Service")

# Register routes
app.include_router(employee.router)
