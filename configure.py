from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseSettings


def ready() -> FastAPI:

    class OpenAPISettings(BaseSettings):
        openapi_url: str = "/openapi.json"

    settings = OpenAPISettings()
    app = FastAPI(openapi_url=settings.openapi_url)

    origins = [
        "https://www.kreimben.com/",
        "https://kreimben.com/",
        "http://localhost:8000",
        "http://localhost",
        "http://127.0.0.1:8000/",
        "http://127.0.0.1/",
    ]
    print("Enrolled origins (CORS)")
    print(origins)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    return app

