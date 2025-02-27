from fastapi import APIRouter
from app.api.v1.account import router as account_router
from app.api.v1.auth import router as auth_router
from app.api.v1.characters import router as char_router
from app.api.v1.room import router as room_router


router = APIRouter()
router.include_router(account_router)
router.include_router(auth_router)
router.include_router(char_router)
router.include_router(room_router)