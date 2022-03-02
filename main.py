# FastAPI.
from fastapi import Request, Response

# Custom.
from configure import *
from event import setting_event
from database import main as db

# Setting base app.
app = FastAPI()
ready(app)
setting_event(app)


@app.get("/get_photos")
async def get_photoes(req: Request):
    urls = db.get_photoes()

    return Response(content=urls, media_type="application/jpg")


@app.get("/update_photos")
async def update_photoes(req: Request):
    urls = db.update_photoes()
    return {
        "success": True,
        "message": "Success to update photoes.",
        "url": urls
    }
