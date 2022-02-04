# FastAPI.
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Custom.
from configure import *
from event import setting_event

# Setting base app.
app = FastAPI()
ready(app)
setting_event(app)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(req: Request):

    # Load saved image from image server.
    urls = []
    results = {"hello", "world!", "Sir.", "Kreimben"}

    r = {
        "request": req,
        "title": "Kreimben.com",
        "elements": [
            "hello, kreimben!"
        ],
        "results": [
            results
        ],
        "urls": urls
    }
    return templates.TemplateResponse("index.html", context=r)