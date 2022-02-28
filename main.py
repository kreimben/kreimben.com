# FastAPI.
from fastapi import Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Custom.
from configure import *
from event import setting_event
from database import main as db

# Setting base app.
app = FastAPI()
ready(app)
setting_event(app)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(req: Request):

    # db.update_photoes()
    # db.save_photoes()
    urls = db.get_photoes()

    r = {
        "request": req,
        "title": "Kreimben.com",
        "elements": [
            "hello, kreimben!"
        ],
        "urls": [
            urls
        ]
    }
    return templates.TemplateResponse("index.html", context=r)

