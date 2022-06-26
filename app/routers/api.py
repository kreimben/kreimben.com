from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

import app.model.crud as crud
import app.model.database as database
import app.utils.google_auth as ga

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
    data = ga.get_secret()

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
    data = ga.get_access_token_from_google(request.query_params['code'])
    access_token = data['access_token']
    response = RedirectResponse(f'/api/user/check_id?access_token={access_token}')
    return response


@router.get('/user/check_id')
async def check_id(access_token: str, db: Session = Depends(get_db)):
    user_info = ga.get_user_info(access_token)

    google_id = user_info['id']

    user = crud.read_user(db, google_id)

    if not user:
        return RedirectResponse(f'/api/user/create?access_token={access_token}')
    else:
        return RedirectResponse(f'/api/user/{google_id}')


@router.get('/user/{id}')
async def get_user_info(id: str, db: Session = Depends(get_db)):
    user = crud.read_user(db, id)

    return user


@router.post('/user/create')
@router.get('/user/create')
async def create_user(access_token: str, db: Session = Depends(get_db)):
    user_info = ga.get_user_info(access_token)

    crud.create_user(db,
                     id=user_info['id'],
                     email=user_info['email'],
                     first_name=user_info['given_name'],
                     last_name=user_info['family_name'],
                     thumbnail_url=user_info['picture'])

    return RedirectResponse(f'/api/user/{user_info["id"]}')
