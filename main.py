from fastapi import FastAPI
from routers.users import router as user_router

app = FastAPI(
     title="FastAPI JWT Auth Example",
    description="User registration, login and JWT auth",
    version="1.0.0"
)

app.include_router(user_router,prefix="/users")
