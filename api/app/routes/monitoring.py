from fastapi import APIRouter, Depends, Header, HTTPException
from app.services.system import get_status
from app.core.config import settings

router = APIRouter()

def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

@router.get("/status", dependencies=[Depends(verify_api_key)])
def status():
    return get_status()