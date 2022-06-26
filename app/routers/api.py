import json

import requests
from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

import app.model.crud as crud
import app.model.database as database

router = APIRouter(prefix='/api', tags=['api'])


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/login')
async def login():
    data = __get_secret()

    client_id = data['web']['client_id']
    redirect_uri = data['web']['redirect_uris'][1]  # Which is `localhost:10120/api/redirect`

    url = data['web']['auth_uri']
    ci = f'?client_id={client_id}'
    ru = f'&redirect_uri={redirect_uri}'
    scope = '&scope=email profile'
    response_type = '&response_type=code'
    access_type = '&access_type=online'

    url += ci + ru + scope + response_type + access_type

    return RedirectResponse(url)


@router.get('/logout')
async def logout(request: Request):
    return {'success': True, 'message': 'Logout feature is currently implementing now!'}


@router.get('/redirect')
async def redirect(request: Request):
    data = __get_access_token_from_google(request.query_params['code'])
    access_token = data['access_token']
    response = RedirectResponse(f'/api/redirect/get_token?access_token={access_token}')
    return response


@router.get('/redirect/get_token')
async def get_token(access_token: str):
    user_info = __get_user_info(access_token)
    return RedirectResponse(f'/api/user/check_id?user_info={user_info}')


@router.get('/user/check_id')
async def check_id(user_info: dict, db: Session = Depends(get_db)):
    google_id = user_info['id']

    user = crud.read_user(db, google_id)
    print('user')
    print(user)
    print(type(user))

    if not user:
        return RedirectResponse(f'/api/user/create?user_info={user_info}')
    else:
        return user


@router.get('/user/create')
async def create_user(user_info: dict, db: Session = Depends(get_db)):
    return crud.create_user(db,
                            id=user_info['id'],
                            email=user_info['email'],
                            first_name=user_info['first_name'],
                            last_name=user_info['last=name'],
                            thumbnail_url=user_info['thumbnail_url'])


def __get_secret():
    data = None
    with open('../google_oauth2_secret.json') as f:
        data = json.load(f)
    return data


def __get_access_token_from_google(code: str):
    data = __get_secret()

    url = data['web']['token_uri']

    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }

    grant_type = '?grant_type=authorization_code'
    code = f"&code={code}"
    client_id = f"&client_id={data['web']['client_id']}"
    client_secret = f"&client_secret={data['web']['client_secret']}"
    redirect_uri = f"&redirect_uri={data['web']['redirect_uris'][1]}"

    url += grant_type + code + client_secret + client_id + redirect_uri

    response = requests.post(url=url, headers=headers)
    json = response.json()

    return json


def __get_user_info(access_token: str) -> dict:
    url = f'https://www.googleapis.com/oauth2/v1/userinfo'
    alt = '?alt=json'
    at = f'&access_token={access_token}'
    scope = f'&scope=https://www.googleapis.com/auth/userinfo.profile'

    url += alt + at + scope

    json = requests.get(url).json()

    # print(f'user info: {json}')

    return json
