from fastapi import FastAPI

def setting_event(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        print("Starting up!")

    @app.on_event("shutdown")
    async def shutdown():
        print("Shutdown!")