from fastapi import APIRouter, HTTPException

from app.schemas.proxy_schemas import ProxyRequest

router = APIRouter()


@router.api_route(
    "/{path:path}",
    methods=["POST", "PUT", "PATCH", "DELETE"]
)
async def method_not_allowed(path: str = ProxyRequest) -> None:
    raise HTTPException(
        status_code=405,
        detail="method not allowed"
    )
