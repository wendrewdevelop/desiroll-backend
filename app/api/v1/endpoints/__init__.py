from fastapi import APIRouter
from app.api.v1.account import router as account_router
from app.api.v1.auth import router as auth_router


router = APIRouter()
router.include_router(account_router)
router.include_router(auth_router)