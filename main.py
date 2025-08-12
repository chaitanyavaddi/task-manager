from fastapi import FastAPI
from src.routes.tasks import router as task_router
from src.routes.auth import router as auth_router

app = FastAPI(title="Todo APP")


app.include_router(task_router)
app.include_router(auth_router)