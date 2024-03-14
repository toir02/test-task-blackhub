from pydantic import BaseModel


class ProxyRequest(BaseModel):
    path: str
