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
    r = {
        "request": req,
        "title": "Kreimben.com",
        "body": "hello, kreimben!"
    }
    return templates.TemplateResponse("index.html", context=r)

@app.get("/test")
@app.post("/test")
async def test_method(req: Request):
    if req.method == "GET":
        return {"method": req.method}
    elif req.method == "POST":
        header = req.headers
        body = await req.body()
        return {"status": "not bad", "comment": "Good!", "body": body}
    else:
        return {"message": "Un recognized method.", "method": req.method}