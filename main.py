# FastAPI.
from fastapi import Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Custom.
from configure import *
from event import setting_event

# Dummy data.
from datetime import datetime
from sqlalchemy.orm import Session

# Database.
from .database import crud, models, schemas
from .database.database import SessionLocal, engine

# Setting base app.
app = FastAPI()
ready(app)
setting_event(app)

templates = Jinja2Templates(directory="templates")


# Setting database.
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def root(req: Request):

    # Load saved image from image server.
    urls = []

    # await fb.write_post(post_id= "sdsdfsdgasdfsdf", param={
    #    "date-time": datetime.now(),
    #    "random_str": ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(10))
    # })

    # results = fb.read_posts()

    r = {
        "request": req,
        "title": "Kreimben.com",
        "elements": [
            "hello, kreimben!"
        ],
        "results": [
            # results
        ],
        "urls": urls
    }
    return templates.TemplateResponse("index.html", context=r)


@app.get("/create_dummy", response_model=schemas.Post)
@app.post("/create_dummy", response_model=schemas.Post)
async def create_dummy_data(post: schemas.Post, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post.id)
    if db_post:
        raise HTTPException(status_code=400, detail="Post already registered!")
    return crud.create_post(db, post=post)
