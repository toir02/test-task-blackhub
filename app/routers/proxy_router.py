import re

from fastapi import APIRouter, HTTPException

from app.schemas.proxy_schemas import ProxyRequest
from app.services.utils import get_page_content

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


@router.get("/{path:path}")
async def get_html_content(
        path: str = ProxyRequest
) -> dict[str, str]:
    content = await get_page_content(path)
    content = re.sub(r'(?i)Black\s*Russia', 'BlackHub Games', content)
    return {
        "message": content
    }
