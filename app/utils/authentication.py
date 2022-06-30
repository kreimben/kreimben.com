from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status, Cookie
from jwt.exceptions import PyJWTError
from pydantic import BaseModel

import app.model.schemas as schemas
from app.utils.env import get_secret_key
from . import errors


class Token(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = 'bearer'


class TokenData(schemas.User):
    pass


def __get_token_principle() -> (str, str):
    secret = get_secret_key()
    algo = 'HS256'

    return secret, algo


def generate_token(user_data: dict, update_access_token: bool = False):
    if update_access_token:
        return Token(access_token=__issue_access_token(user_data, timedelta(hours=1)))
    else:
        return Token(access_token=__issue_access_token(user_data, timedelta(hours=1)),
                     refresh_token=__issue_refresh_token(user_data, timedelta(days=60)))


def __issue_access_token(user_data: dict, expires_delta: timedelta | None = None) -> jwt:
    secret, algo = __get_token_principle()

    to_encode = user_data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)

    to_encode.update({'exp': expire, 'iat': datetime.utcnow()})

    encoded_jwt = jwt.encode(to_encode, secret, algorithm=algo)
    return encoded_jwt


def __issue_refresh_token(user_data: dict, expires_delta: timedelta | None = None) -> jwt:
    secret, algo = __get_token_principle()

    to_encode = user_data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=60)

    to_encode.update({'exp': expire, 'iat': datetime.utcnow()})

    encoded_jwt = jwt.encode(to_encode, secret, algorithm=algo)
    return encoded_jwt


def __ready_exception_unauthorized(detail: str | None = None) -> HTTPException:
    # print(f'detail: {detail}')

    if detail is None:
        detail = 'Could not validate credentials'
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"},
    )


def __try_get_payload_in_token(token: str) -> jwt:
    secret, algo = __get_token_principle()
    try:
        return jwt.decode(token, secret, algorithms=[algo])
    except jwt.PyJWTError as e:
        print(f'jwt decode error: {e.__repr__()}')
        print(f'token: {token}')
        raise errors.TokenExpired(status.HTTP_401_UNAUTHORIZED)


def __try_check_exp(at: str, rt: str) -> bool:
    """
    Validate expiration both tokens.
    :param at: Access Token
    :param rt: Refresh Token
    :return: True=Both tokens are valid. False=Access token is expired.
    """
    if __try_get_payload_in_token(rt) is None:
        raise __ready_exception_unauthorized(detail='Refresh Token Expired!')
    else:
        # If refresh_token is still valid, Check about access_token.
        if __try_get_payload_in_token(at) is None:
            return False
        else:
            return True


def try_extract_user_data_in_token(token: str) -> TokenData:
    try:
        payload = __try_get_payload_in_token(token)
    except PyJWTError as e:
        print(f'Token is not validated: {e.__repr__()}')
        print('try_extract_user_data_in_token')
        raise __ready_exception_unauthorized(detail='User id is not valid.')

    except errors.TokenExpired as e:
        print(f'try_extract_user_data_in_token: {e.__repr__()}')
        raise errors.TokenExpired(status.HTTP_401_UNAUTHORIZED)

    return TokenData(**payload)


# Dependency
def try_is_valid_token(access_token: str = Cookie(),
                       refresh_token: str = Cookie()) -> bool:
    """
    When tokens are valid, Return `True`.
    When access token is not valid, Return `False`.
    When refresh token is not valid, raise `HTTPException`.

    :param access_token:
    :param refresh_token:
    :return:
    """

    if __try_get_payload_in_token(refresh_token) is None:
        print(f'in validate refresh token')
        raise errors.RefreshTokenExpired(status.HTTP_401_UNAUTHORIZED)

    if __try_get_payload_in_token(access_token) is None:
        print(f'in validate access token')
        raise errors.AccessTokenExpired(status.HTTP_401_UNAUTHORIZED)
