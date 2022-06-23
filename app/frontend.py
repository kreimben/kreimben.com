import http

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response
from starlette.templating import Jinja2Templates
import model.crud as crud
import model.database as database

router = APIRouter(
    tags=['front']
)
templates = Jinja2Templates(directory='templates')

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/')
async def entry(request: Request, night_mode: bool | None = None):
    param = {
        'request': request,
        'title': 'Kreimben.com',
        'night_mode': night_mode
    }
    return templates.TemplateResponse('index.html', context=param)

@router.get('/blog')
async def blog_main(request: Request, night_mode: bool | None = None, db: Session = Depends(get_db)):
    # Ready for data from database (SQLite).
    posts = crud.read_posts(db)

    # Ready for parameters.
    param = {
        'request': request,
        'title': 'Kreimben\'s Blog',
        'posts': posts,
        'night_mode': night_mode
    }
    return templates.TemplateResponse('blog.html', context=param)


@router.get('/blog/{uuid}')
async def post(request: Request, uuid: str, night_mode: bool | None = None, db: Session = Depends(get_db)):
    # Ready for data from database (SQLite).
    post = crud.read_post(db, uuid)

    if post is None:
        templates.TemplateResponse('wrong_page.html')

    # Ready for paramters.
    param = {
        'request': request,
        'night_mode': night_mode
    }

    return templates.TemplateResponse('blog.html', context=param)
