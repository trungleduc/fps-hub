from fastapi import APIRouter, Request
from fps.hooks import register_router

r = APIRouter()


@r.get("/oauth_callback")
async def cb(request: Request):

    return {"ok": True}


router = register_router(r)
