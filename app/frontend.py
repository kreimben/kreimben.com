from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
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
async def entry(request: Request):
    param = {
        'request': request,
        'title': 'Kreimben.com',
        'login': False
    }
    return templates.TemplateResponse('index.html', context=param)


@router.get('/blog')
async def blog_main(request: Request, db: Session = Depends(get_db)):
    # Ready for data from database (SQLite).
    posts = crud.read_posts(db)

    # Ready for parameters.
    param = {
        'request': request,
        'title': 'Kreimben\'s Blog',
        'posts': posts,
        'login': False
    }
    return templates.TemplateResponse('blog.html', context=param)


@router.get('/blog/{uuid}')
async def post(request: Request, uuid: str, db: Session = Depends(get_db)):
    # Ready for data from database (SQLite).
    post = crud.read_post(db, uuid)

    if post is None:
        templates.TemplateResponse('wrong_page.html')

    # Ready for paramters.
    param = {
        'request': request,
        'login': False
    }

    return templates.TemplateResponse('blog.html', context=param)
