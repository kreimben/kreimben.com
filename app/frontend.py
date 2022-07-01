from fastapi import APIRouter, Depends, Cookie
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

import app.utils.authentication as authentication
import app.utils.errors as errors
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


@router.get('/blog', tags=['blog'])
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


@router.get('/blog/{post_id}', tags=['blog'])
async def post(request: Request, post_id: str, db: Session = Depends(database.get_db)):
    # Ready for data from database (SQLite).
    post = crud.read_post(db, post_id)

    if post is None:
        return templates.TemplateResponse('wrong_page.html', context={'request': request})

    # Ready for paramters.
    param = {
        'request': request,
        'login': False
    }

    return templates.TemplateResponse('blog.html', context=param)


@router.get('/user/{user_id}', tags=['user'])
async def get_user_page(request: Request, user_id: str,
                        access_token: str | None = Cookie(None), refresh_token: str | None = Cookie(None),
                        db: Session = Depends(database.get_db)):
    if access_token is None or refresh_token is None:
        return RedirectResponse('/api/login')

    try:
        # Validate given token.
        if not authentication.try_is_valid_token(access_token, refresh_token):
            # access_token is expired.
            response = RedirectResponse(f'/api/update_access_token?user_id={user_id}&callback_uri=/user/{user_id}')
            return response

        # Check user from db.
        user = crud.read_user(db, user_id=user_id)
        param = {
            'request': request,
            'user_info': user
        }
        return templates.TemplateResponse('user.html', context=param)

    except errors.AccessTokenExpired as _:
        # Update access token using refresh token.
        return RedirectResponse('/api/auth/update_access_token')

    except errors.RefreshTokenExpired as _:
        # Delete tokens and re-login.
        return RedirectResponse('/api/auth/revoke_token?callback_uri=/api/login')

    except errors.DBError as _:
        # When user never exists in database.
        return RedirectResponse('/api/login')
