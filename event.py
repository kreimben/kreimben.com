# FastAPI
from fastapi import FastAPI

# Custom
import database.firebase


def setting_event(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        print("Starting up!")

        fs = database.firebase.init_firebase_admin_sdk()
        #if _check_firebase_admin(fs.credential) is False:
            # TODO: Write debug code. (Instead of normal print)
            #print("Credential Error")

    @app.on_event("shutdown")
    async def shutdown():
        print("Shutdown!")


def _check_firebase_admin(cred) -> bool:
    if cred is not None:
        return True
    else:
        return False
