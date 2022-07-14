from fastapi import Cookie
from pydantic import BaseModel

import app.model.schemas as schemas
from .errors import AccessTokenExpired, RefreshTokenExpired


class Token(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = 'bearer'


class TokenData(schemas.User):
    pass


from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
from jwt import InvalidAlgorithmError, ImmatureSignatureError, InvalidIssuedAtError, \
    InvalidIssuerError, InvalidAudienceError, ExpiredSignatureError, InvalidSignatureError
from jwt import encode, decode


def issue_token(user_info: dict, delta: timedelta):
    """
    This function doesn't take care of errors!

    :param user_info:
    :param delta:
    :return:
    """
    payload = user_info.copy()

    payload.update({'iat': datetime.now(tz=timezone.utc), 'exp': datetime.now(tz=timezone.utc) + delta})

    jwt = encode(payload=payload, key='secret_key', algorithm='HS256')

    return jwt


def extract_payload_from_token(token: str):
    """
    This function doesn't take care of errors!

    :param token:
    :return:
    """
    payload = decode(jwt=token, key='secret_key', algorithms=['HS256'])

    return payload


# Dependency
def check_auth_using_token(access_token: str | None = Cookie(None),
                           refresh_token: str | None = Cookie(None)):
    # Check tokens are fine.
    if access_token is None or refresh_token is None:
        return

    # Check `refresh_token` first.
    try:
        payload = extract_payload_from_token(refresh_token)

        # Check `access_token` second.
        try:
            payload = extract_payload_from_token(access_token)
            return payload
        # Unacceptable error.
        except InvalidAlgorithmError as e:
            raise HTTPException(detail=f'JWT Error (InvalidAlgorithmError/{e.__repr__()})', status_code=401)
        except ImmatureSignatureError as e:
            raise HTTPException(detail=f'JWT Error (ImmatureSignatureError/{e.__repr__()})', status_code=401)
        except InvalidIssuerError as e:
            raise HTTPException(detail=f'JWT Error (InvalidIssuerError/{e.__repr__()})', status_code=401)
        except InvalidAudienceError as e:
            raise HTTPException(detail=f'JWT Error (InvalidAudienceError/{e.__repr__()})', status_code=401)
        except InvalidSignatureError as e:
            raise HTTPException(detail=f'JWT Error (InvalidSignatureError/{e.__repr__()})', status_code=401)
        except InvalidIssuedAtError as e:  # When `iat` is future.
            raise HTTPException(detail=f'JWT Error (InvalidIssuedAtError/{e.__repr__()})', status_code=401)

        # Acceptable error. Should re-issue token.
        except ExpiredSignatureError:
            return AccessTokenExpired()

    # Unacceptable error.
    except InvalidAlgorithmError as e:
        raise HTTPException(detail=f'JWT Error (InvalidAlgorithmError/{e.__repr__()})', status_code=401)
    except ImmatureSignatureError as e:
        raise HTTPException(detail=f'JWT Error (ImmatureSignatureError/{e.__repr__()})', status_code=401)
    except InvalidIssuerError as e:
        raise HTTPException(detail=f'JWT Error (InvalidIssuerError/{e.__repr__()})', status_code=401)
    except InvalidAudienceError as e:
        raise HTTPException(detail=f'JWT Error (InvalidAudienceError/{e.__repr__()})', status_code=401)
    except InvalidSignatureError as e:
        raise HTTPException(detail=f'JWT Error (InvalidSignatureError/{e.__repr__()})', status_code=401)
    except InvalidIssuedAtError as e:  # When `iat` is future.
        raise HTTPException(detail=f'JWT Error (InvalidIssuedAtError/{e.__repr__()})', status_code=401)

    # Acceptable error. Should re-issue token.
    except ExpiredSignatureError:
        return RefreshTokenExpired()
    except AccessTokenExpired:
        return AccessTokenExpired()
