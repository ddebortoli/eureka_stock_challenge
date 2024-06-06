from fastapi import APIRouter, Depends, Body

from app.auth.token import verify_token
from app.backend.users.users import Users
from app.models.users import Client

router = APIRouter()

@router.post("/user")
def create_user(current_user: dict = Depends(verify_token), client: Client = Body(...)):
    user_handler = Users()
    return user_handler.create_client(client)
