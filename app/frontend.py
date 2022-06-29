from fastapi import APIRouter, Depends, HTTPException, Cookie
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

import app.utils.authentication as authentication
import model.crud as crud
import model.database as database

router = APIRouter(
    tags=['front']
)
templates = Jinja2Templates(directory='templates')


@router.get('/')
async def entry(request: Request):
    param = {
        'request': request,
        'title': 'Kreimben.com',
        'login': False
    }
    return templates.TemplateResponse('index.html', context=param)


@router.get('/blog')
async def blog_main(request: Request, db: Session = Depends(database.get_db)):
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
async def post(request: Request, uuid: str, db: Session = Depends(database.get_db)):
    # Ready for data from database (SQLite).
    post = crud.read_post(db, uuid)

    if post is None:
        return templates.TemplateResponse('wrong_page.html', context={'request': request})

    # Ready for paramters.
    param = {
        'request': request,
        'login': False
    }

    return templates.TemplateResponse('blog.html', context=param)


@router.get('/user/{google_id}')
async def get_user_page(google_id: str, request: Request, user_info=Depends(app.routers.api.get_user_info)):
    param = {
        'request': request,
        'user_info': user_info
    }
    return templates.TemplateResponse('user.html', context=param)
