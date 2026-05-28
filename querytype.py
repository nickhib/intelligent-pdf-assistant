from pydantic import BaseModel
from fastapi import APIRouter, Request
## fastapi needs To declare a request body, you use Pydantic models with all their power and benefits.
## https://fastapi.tiangolo.com/tutorial/body/
class QueryReq(BaseModel):
    query: str