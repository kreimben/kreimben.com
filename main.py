# FastAPI.
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Custom.
from configure import *
from event import setting_event
import Instagram

# Setting base app.
app = FastAPI()
ready(app)
setting_event(app)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(req: Request):
    media = Instagram.get_user_media()
    urls = []
    for e in media["data"]:
        e_id = Instagram.get_representative_media_id(e["id"])
        datas = Instagram.get_media_children(e_id)["data"]
        for data in datas:
            print("data: ", data)
            urls.append(data["media_url"])

    r = {
        "request": req,
        "title": "Kreimben.com",
        "elements": [
            "hello, kreimben!"
        ],
        "results": [
            id
        ],
        "urls": urls
    }
    return templates.TemplateResponse("index.html", context=r)