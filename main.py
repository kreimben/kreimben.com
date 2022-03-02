# FastAPI.
from fastapi import Request

# Custom.
from configure import *
from event import setting_event
from database import main as db

# Setting base app.
app = FastAPI()
ready(app)
setting_event(app)


@app.get("/get_photoes")
async def get_photoes(req: Request):
    urls = db.get_photoes()

    return urls

@app.get("/update_photoes")
async def update_photoes(req: Request):
    db.update_photoes()
    return {"success": True, "message": "Success to update photoes."}
