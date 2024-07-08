from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException, Security
from .schemas import User

security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "user" or credentials.password != "password":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return User(username=credentials.username)
