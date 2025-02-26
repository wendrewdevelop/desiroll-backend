from fastapi import APIRouter
from app.api.v1.account import router as account_router


router = APIRouter()
router.include_router(account_router)