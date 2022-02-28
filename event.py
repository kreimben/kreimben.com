# FastAPI
from fastapi import FastAPI


def setting_event(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        print("Starting up!")

    @app.on_event("shutdown")
    async def shutdown():
        print("Shutdown!")


def _check_firebase_admin(cred) -> bool:
    if cred is not None:
        return True
    else:
        return False
