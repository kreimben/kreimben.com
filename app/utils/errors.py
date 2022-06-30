from fastapi import HTTPException


class DBError(ValueError):
    def __init__(self, detail: str):
        self.detail = detail


class TokenExpired(HTTPException):
    pass


class AccessTokenExpired(TokenExpired):
    pass


class RefreshTokenExpired(TokenExpired):
    pass
