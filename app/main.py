from fastapi import FastAPI
from app.database.database import init_db
from app.routes import user
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    print("Application startup complete")

    yield  

    print("Application shutdown")

app = FastAPI(lifespan=lifespan)
app.include_router(user.router)
