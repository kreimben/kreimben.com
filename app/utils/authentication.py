from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status, Cookie
from jwt.exceptions import PyJWTError
from pydantic import BaseModel

from app.utils.env import get_secret_key


class Token(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = 'bearer'


import app.model.schemas as schemas


class TokenData(schemas.User):
    pass


def __get_token_principle() -> (str, str):
    secret = get_secret_key()
    algo = 'HS256'

    return secret, algo


def generate_token(user_data: dict, expires_delta: timedelta | None = None):
    token = Token(access_token=__issue_access_token(user_data, expires_delta),
                  refresh_token=__issue_refresh_token(user_data, expires_delta),
                  token_type='bearer')

    return token


def __issue_access_token(user_data: dict, expires_delta: timedelta | None = None):
    secret, algo = __get_token_principle()

    to_encode = user_data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)

    to_encode.update({'exp': expire, 'iat': datetime.utcnow()})

    encoded_jwt = jwt.encode(to_encode, secret, algorithm=algo)
    return encoded_jwt


def __issue_refresh_token(user_data: dict, expires_delta: timedelta | None = None):
    secret, algo = __get_token_principle()

    to_encode = user_data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=60)

    to_encode.update({'exp': expire, 'iat': datetime.utcnow()})

    encoded_jwt = jwt.encode(to_encode, secret, algorithm=algo)
    return encoded_jwt


# TODO: Should be tested.
def is_valid_token(db: Session, token: str) -> bool:
    secret, algo = __get_token_principle()

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, secret, algorithms=[algo])
        # print(f'payload keys: {payload.keys()}')
        # print(f'payload values: {payload.values()}')

        user_id: str = payload.get("id")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(**payload)
    except PyJWTError:
        raise credentials_exception

    # Read user data from database DIRECTLY.
    user = crud.read_user(db, token_data.id)

    if user is None:
        raise credentials_exception
    return True
