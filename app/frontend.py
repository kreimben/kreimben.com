from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

import app.utils.authentication as authentication
import app.utils.errors as errors
import model.crud as crud
import model.database as database
from app.utils.authentication import is_login

router = APIRouter(
    tags=['front']
)
templates = Jinja2Templates(directory='templates')


@router.get('/')
async def entry(request: Request, login=Depends(is_login)):
    param = {
        'request': request,
        'title': 'Kreimben.com',
        'login': login
    }
    return templates.TemplateResponse('index.html', context=param)


@router.get('/blog', tags=['blog'])
async def blog_main(request: Request, db: Session = Depends(database.get_db), login=Depends(is_login)):
    # Ready for data from database (SQLite).
    posts = crud.read_posts(db)

    # Ready for parameters.
    param = {
        'request': request,
        'title': 'Kreimben\'s Blog',
        'posts': posts,
        'login': login
    }
    return templates.TemplateResponse('blog.html', context=param)


@router.get('/blog/write', tags=['blog'])
async def write_post(request: Request, login=Depends(is_login)):
    # Ready for parameters.
    param = {
        'request': request,
        'login': login
    }

    return templates.TemplateResponse('write_post.html', context=param)


@router.get('/blog/{post_id}', tags=['blog'])
async def post(request: Request, post_id: str, db: Session = Depends(database.get_db), login=Depends(is_login)):
    # Ready for data from database (SQLite).
    post = crud.read_post(db, post_id)

    if post is None:
        return templates.TemplateResponse('wrong_page.html', context={'request': request})

    # Ready for parameters.
    param = {
        'request': request,
        'login': login
    }

    return templates.TemplateResponse('blog.html', context=param)


@router.get('/user/{user_id}', tags=['user'])
async def get_user_page(request: Request, user_id: str,
                        payload=Depends(authentication.check_auth_using_token),
                        db: Session = Depends(database.get_db),
                        login=Depends(is_login)):
    if payload is None or \
            isinstance(payload, errors.AccessTokenExpired) or \
            isinstance(payload, errors.RefreshTokenExpired):
        return RedirectResponse('/api/login')

    # Check user from db.
    user = crud.read_user(db, user_id=user_id)
    param = {
        'request': request,
        'user_info': user,
        'login': login
    }
    return templates.TemplateResponse('user.html', context=param)
