from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def ready(app: FastAPI):
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
