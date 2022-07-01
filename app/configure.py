from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import model.database as database
import model.models as models


def __set_cors(app: FastAPI) -> FastAPI:
    print("Enrolled origins (CORS)")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    return app


def __configure_database():
    engine = database.engine
    models.Base.metadata.create_all(bind=engine)
    print('Ready for database!')


def ready() -> FastAPI:
    app = FastAPI(
        title="www.kreimben.com server",
        description="This is server for www.kreimben.com",
        version="2.0.0",
    )

    # docs_url=None,
    # redoc_url=None

    app = __set_cors(app)
    __configure_database()

    return app
