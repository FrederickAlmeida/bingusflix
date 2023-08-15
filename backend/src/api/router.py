from fastapi import APIRouter

from api import users
from api import login

api_router = APIRouter()
api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(login.router, prefix='/login', tags=['login'])
