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
async def redirect(code: str, db: Session = Depends(get_db)):
    data = ga.get_access_token_from_google(code)
    access_token = data['access_token']

    user_info = ga.get_user_info(access_token)
    google_id = user_info['id']

    try:
        crud.read_user(db, google_id)
        return RedirectResponse(f'/api/user/{google_id}')
    except ValueError as _:
        # print(f'no such user in /redirect function: {e.__repr__()}')
        return RedirectResponse(f'/api/user/create?access_token={access_token}')


@router.post('/user/create')
@router.get('/user/create')
async def create_user(access_token: str, db: Session = Depends(get_db)):
    user_info = ga.get_user_info(access_token)
    print('create_user function.')
    try:
        user = crud.create_user(db,
                                id=user_info['id'],
                                email=user_info['email'],
                                first_name=user_info['given_name'],
                                last_name=user_info['family_name'],
                                thumbnail_url=user_info['picture'])
        return RedirectResponse(f'/api/user/{user.id}')

    except ValueError as e:
        print(f'value error in create_user function: {e.__repr__()}')
        return {
            'success': False,
            'message': e.__repr__()
        }


@router.get('/user/{google_id}')
async def get_user_info(google_id: str, db: Session = Depends(get_db)):
    try:
        user = crud.read_user(db, google_id)
        return {
            'success': True,
            'user': user
        }
    except ValueError as e:
        print(f'no such user in /user/google_id fucntion: {e.__repr__()}')
        return {
            'success': False,
            'message': e.__repr__()
        }


@router.put('/user/update/{google_id}')
@router.get('/user/update/{google_id}')
async def update_user(google_id: str, first_name: str, last_name: str, email: str, db: Session = Depends(get_db)):
    try:
        user = crud.update_user(db,
                                id=google_id,
                                first_name=first_name,
                                last_name=last_name,
                                email=email)
        return {
            'success': True,
            'message': 'User Updated.',
            'user': user
        }
    except ValueError as e:
        return {
            'success': False,
            'message': e.__repr__()
        }


@router.delete('/user/delete/{google_id}')
@router.get('/user/delete/{google_id}')
async def delete_user(google_id: str, db: Session = Depends(get_db)):
    try:
        crud.delete_user(db, google_id)
        return {
            'success': True,
            'message': 'User Deleted.'
        }
    except ValueError as e:
        return {
            'success': False,
            'message': e.__repr__()
        }


@router.post('authorization/create/{name}')
@router.get('authorization/create/{name}')
async def create_authorization(name: str, db: Session = Depends(get_db)):
    try:
        crud.create_authorization(db, name=name)
        return {
            'success': True,
            'message': 'Authorization Created.',
            'name': name
        }
    except ValueError as e:
        return {
            'success': False,
            'message': e.__repr__()
        }
