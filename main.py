from fastapi import FastAPI

from app.routers.proxy_router import router

app = FastAPI()

app.include_router(router)
