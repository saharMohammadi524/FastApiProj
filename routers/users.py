from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.engine import get_db
from oprations.users import UsersOpration
from schema._input import DeleteUserAccountInput, RegisterInput, UpdateUserProfileInput
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

@router.post("/register")
def user_register(data: RegisterInput, db: Session = Depends(get_db)):
    user = UsersOpration(db).create(username=data.username, password=data.password)
    return user

@router.get("/")
async def user_profile(username:str,db: Session = Depends(get_db)):
    user_profile = UsersOpration(db).get_by_username(username)
    return user_profile

@router.put("/")
async def user_update(data: UpdateUserProfileInput, db: Session = Depends(get_db)):
    user_update= UsersOpration(db).update_username(data.old_username, data.new_username)
    return user_update

@router.delete("/")
async def user_delete(data:DeleteUserAccountInput, db: Session = Depends(get_db)):
    user_delete= UsersOpration(db).user_delete_account(data.username,data.password)
    return user_delete

@router.post("/")
async def user_login_checker(data: RegisterInput, db: Session = Depends(get_db)):
    token= UsersOpration(db).check_user_login(data.username,data.password)
    return token