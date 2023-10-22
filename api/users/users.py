from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from users.models.users import User_Request, User_Response
from database.connect import db
from .schemas.schemas_users import schema_user

app = APIRouter(prefix="/users")

auth = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = 'secret'
ALGORITHM = 'HS256'



def create_token(username:str):
    expire = datetime.utcnow() + timedelta(minutes=30)
    token = jwt.encode({"sub":username, "exp":expire}, SECRET_KEY, ALGORITHM)
    return token


async def get_user_token(token: str = Depends(auth)):
    try:
        user = jwt.decode(token, SECRET_KEY).get("sub")
        user_db = db.store.users.find_one({"username":user})
        return User_Request(**schema_user(user_db))
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error de identificacion")


@app.get("/", response_model= User_Request, status_code=status.HTTP_200_OK)
async def read_users_me(
    current_user: User_Request = Depends(get_user_token)
):
    return current_user

@app.post("/token", response_model= dict, status_code=status.HTTP_201_CREATED)
async def token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = db.store.users.find_one({"username":form_data.username})
    if user:
        if pwd_context.verify(form_data.password, user.get("password")):
            token = create_token(form_data.username)
            return {"access_token": token, "type":"bearer"}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Username o password incorrectas")            
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Username o password incorrectas")