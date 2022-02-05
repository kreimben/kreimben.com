# FastAPI.
import random
import string

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Custom.
from configure import *
from event import setting_event
import database.firebase as fb

from datetime import datetime

# Setting base app.
app = FastAPI()
ready(app)
setting_event(app)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(req: Request):

    # Load saved image from image server.
    urls = []

    await fb.write_post(post_id= "sdsdfsdgasdfsdf", param={
        "date-time": datetime.now(),
        "random_str": ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(10))
    })

    results = fb.read_posts()

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
