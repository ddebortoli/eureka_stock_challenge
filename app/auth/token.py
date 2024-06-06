from jose import JWTError
from fastapi import Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
from app.utils.services.database import Sqlite
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_token(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        sql_handler = Sqlite()
        user_data = sql_handler.get_user_data(token)
        if not user_data:
            raise JWTError('User not found')

        return user_data
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def authenticate_user(api_key: str = Header(...)) -> dict:
    try:
        if not api_key:
            raise HTTPException(status_code=401, detail="API key was not given.")

        sql_handler = Sqlite()
        user_data = sql_handler.get_access_by_client_api_key(api_key)
        if user_data:
            return user_data
        else:
            raise HTTPException(status_code=401, detail="Wrong API key")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal webservice error.")