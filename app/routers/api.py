from datetime import timedelta

from fastapi import APIRouter, Depends, Cookie
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse, JSONResponse
from sqlalchemy.orm import Session

import app.model.crud as crud
import app.model.database as database
import app.utils.authentication as authentication
import app.utils.errors as errors
import app.utils.google_auth as ga

router = APIRouter(prefix='/api', tags=['api'])


@router.get('/login', tags=['login process'])
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


@router.get('/logout', tags=['login process'])
async def logout():
    response = RedirectResponse('/')

    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')

    return response


@router.get('/redirect', tags=['login process'])
async def redirect(code: str, db: Session = Depends(database.get_db),
                   payload=Depends(authentication.check_auth_using_token)):
    """
    This route only be used when user tries to login with google OAuth2.
    Must be submitted with code issued by Google.
    """

    data = ga.get_access_token_from_google(code)
    google_access_token = data['access_token']
    user_info = ga.get_user_info(google_access_token)

    print(f'payload: {payload}')
    if isinstance(payload, errors.AccessTokenExpired) or isinstance(payload, errors.RefreshTokenExpired):
        # If tokens are expired (even if one of them), Just revoke token and regenerate token.
        return RedirectResponse(f'/api/auth/revoke_token?callback_uri=/api/login')
    elif crud.read_user(db=db, google_id=user_info['id']) is None:
        # When no user info in db. (Not registered.)
        return RedirectResponse(f'/api/user/create?google_access_token={google_access_token}')
    elif payload is None and crud.read_user(db=db, google_id=user_info['id']) is not None:
        # When tokens are not saved in cookie and user data is in database.
        return RedirectResponse(f'/api/auth/generate_token?google_id={user_info["id"]}')
    else:
        return RedirectResponse(f'/user/{payload.user_id}')


@router.post('/user/create', status_code=201, tags=['user'])
@router.get('/user/create', status_code=201)
async def create_user(google_access_token: str, db: Session = Depends(database.get_db)):
    user_info = ga.get_user_info(google_access_token)

    # Create user data in DB.
    user = crud.create_user(db,
                            google_id=user_info['id'],
                            email=user_info['email'],
                            first_name=user_info['given_name'],
                            last_name=user_info['family_name'],
                            thumbnail_url=user_info['picture'])
    print(f'user after crud.create_user: {user}')
    return RedirectResponse(f'/api/auth/generate_token?google_id={user.google_id}')


@router.get('/auth/generate_token', tags=['auth'])
async def generate_token(google_id: str, db: Session = Depends(database.get_db)):
    user = crud.read_user(db=db, google_id=google_id)
    dict_user = jsonable_encoder(user)

    # Issue token
    access_token = authentication.issue_token(dict_user, timedelta(hours=1))
    refresh_token = authentication.issue_token(dict_user, timedelta(days=14))

    response = RedirectResponse(f'/user/{user.user_id}')

    # Save access_token and refresh_token to cookie.
    response.set_cookie(key='access_token', value=access_token, secure=True)
    response.set_cookie(key='refresh_token', value=refresh_token, secure=True)

    # Save refresh_token to database.
    try:
        crud.update_user(db,
                         user_id=user.user_id,
                         email=user.email,
                         first_name=user.first_name,
                         last_name=user.last_name,
                         refresh_token=refresh_token)
    except errors.DBError as e:
        print(f'generate token: {e.__repr__()}')
        return {
            'success': False,
            'message': e.__str__()
        }

    return response


@router.get('/auth/revoke_token', tags=['auth'])
async def revoke_token(callback_uri: str | None = None, refresh_token: str = Cookie(...),
                       db: Session = Depends(database.get_db)):
    """
    Remove tokens in cookie and database. After that, Redirect to home.
    """

    response = RedirectResponse(callback_uri) if callback_uri is None else JSONResponse(content={
        'success': True, 'message': 'Successfully Revoked.'
    })

    try:
        user = crud.read_user(db, refresh_token=refresh_token)

        # Delete refresh token in database.
        crud.update_user(db, user.user_id,
                         email=user.email,
                         first_name=user.first_name,
                         last_name=user.last_name,
                         refresh_token=None)

        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return response

    except errors.DBError as e:
        print(f'revoke token: {e.__repr__()}')
        return RedirectResponse('/api/logout')


@router.get('/authorization/create', tags=['authorization'], status_code=201)
@router.post('/authorization/create', tags=['authorization'], status_code=201)
async def create_authorization(name: str, db: Session = Depends(database.get_db)):
    try:
        authoriztion = crud.create_authorization(db, name)
    except errors.DBError as e:
        print(f'create_authorization: {e.__repr__()}')
        authoriztion = crud.read_authorization(db, name)
        return {
            'success': True,
            'message': e.__str__(),
            'authorization': authoriztion
        }

    return {
        'success': True,
        'message': 'Successfully Created.',
        'authorization': authoriztion
    }


@router.get('/authorization/delete/{name}', tags=['authorization'])
@router.delete('/authorization/delete/{name}', tags=['authorization'])
async def delete_authorization(name: str, db: Session = Depends(database.get_db)):
    try:
        num = crud.delete_authorization(db, name)
        return {
            'success': True,
            'message': 'Successfully Deleted.',
            'count': num
        }
    except errors.DBError as e:
        return {
            'success': False,
            'message': e.__str__()
        }
