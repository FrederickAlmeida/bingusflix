from fastapi import APIRouter, HTTPException
from src.schemas.user import UserDB, UserModelPublic
from src.schemas.recovery import AccountRecovery, PasswordChangeResponse

from .users import database

router = APIRouter()

@router.put(
    "/", status_code=200 , response_model=PasswordChangeResponse, tags=["account recovery"]
)
def change_password(account_recovery: AccountRecovery):
    for user in database: # procura um usuário com email e senha iguail ao do formulário
        if user.email == account_recovery.email: # caso o email exista na base de dados e a senha seja igual a confirmação, atualiza a senha do usuário
            if account_recovery.new_password == account_recovery.confirm_password: 
                user.passwd = account_recovery.new_password
                return PasswordChangeResponse(email=user.email, new_password=user.passwd, confirm_password=user.passwd)
            else:
                raise HTTPException(status_code=400, detail="Passwords do not match") # se as senhas digitadas forem diferentes: erro 400
    
    raise HTTPException(status_code=404, detail="User not found") # se não encontrar o usuário: erro 404