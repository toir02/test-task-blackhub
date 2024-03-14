from fastapi import FastAPI

from app.routers.proxy_router import proxy_router

app = FastAPI()

app.include_router(proxy_router)
