from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status, Cookie
from jwt.exceptions import PyJWTError
from pydantic import BaseModel

import app.model.schemas as schemas
from app.utils.env import get_secret_key


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
        return Token(access_token=__issue_access_token(user_data, timedelta(minutes=3)))
    else:
        return Token(access_token=__issue_access_token(user_data, timedelta(minutes=3)),
                     refresh_token=__issue_refresh_token(user_data, timedelta(minutes=5)))


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
    print(f'detail: {detail}')

    if detail is None:
        detail = 'Could not validate credentials'
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"},
    )


def __get_payload_in_token(token: str) -> jwt:
    secret, algo = __get_token_principle()
    print(f'token: {token}')
    try:
        jwt.decode(token, secret, algorithms=[algo])
    except PyJWTError as e:
        print(f'jwt decode error: {e.__repr__()}')


def __check_exp(at: str, rt: str) -> bool:
    """
    Validate expiration both tokens.
    :param at: Access Token
    :param rt: Refresh Token
    :return: True=Both tokens are valid. False=Access token is expired.
    """
    now = datetime.utcnow()

    rtp = __get_payload_in_token(rt)
    rt_exp = datetime.utcfromtimestamp(rtp.get('exp'))
    print(f'exp: {rt_exp}')
    print(f'now: {now}')
    if rt_exp < now:
        # If refresh_token is expired
        raise __ready_exception_unauthorized()
    else:
        # If refresh_token is still valid, Check about access_token.
        atp = __get_payload_in_token(at)
        at_exp = datetime.utcfromtimestamp(atp.get('exp'))
        print(f'exp: {at_exp}')
        print(f'now: {now}')

        if at_exp < now:  # Access token is expired.
            return False
        else:  # When both tokens are valid.
            return True


def __extract_user_data_in_token(token: str) -> TokenData:
    payload = __get_payload_in_token(token)

    user_id: str = payload.get("id")
    if user_id is None:
        raise __ready_exception_unauthorized()
    return TokenData(**payload)


def is_valid_token(access_token: str = Cookie(),
                   refresh_token: str = Cookie()) -> bool:
    try:
        results = __check_exp(access_token, refresh_token)
        token_data = __extract_user_data_in_token(access_token)
    except PyJWTError:
        raise __ready_exception_unauthorized()

    return results
