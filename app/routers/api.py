from fastapi import APIRouter, Depends, HTTPException, Cookie
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
async def redirect(code: str,
                   access_token: str | None = Cookie(None), refresh_token: str | None = Cookie(None)):
    """
    This route only be used when user tries to login with google OAuth2.
    Must be submitted with code issued by Google.

    :param code: Code issued by Google.
    :param access_token: Issued by this server.
    :param refresh_token: Issued by this server.
    :param db: SQLite Database Session.
    :return:
    """

    data = ga.get_access_token_from_google(code)
    google_access_token = data['access_token']

    # First. Check having tokens. (issued by this server.)
    if access_token is None or refresh_token is None:
        # Just go to create user.
        return RedirectResponse(f'/api/user/create?google_access_token={google_access_token}')

    try:
        # Second. If tokens exist, Check its' validation.
        is_valid = authentication.try_is_valid_token(access_token, refresh_token)

        if is_valid:
            # If access_token is valid, Go to user page.
            user = authentication.try_extract_user_data_in_token(access_token)
            return RedirectResponse(f'/user/{user.user_id}')  # TODO: redirect to home.
        else:
            # If access_token is not valid, Go to update access_token.
            return RedirectResponse(f'/api/update_access_token')

    except HTTPException as e:
        # If access_token and refresh_token are not valid, Go to revoke tokens.
        print(f'redirect exception: ${e.__repr__()}')
        return RedirectResponse(f'/api/auth/revoke_token?callback_uri=/api/login')


@router.post('/user/create', status_code=201, tags=['user'])
@router.get('/user/create', status_code=201)
async def create_user(google_access_token: str, db: Session = Depends(database.get_db)):
    user_info = ga.get_user_info(google_access_token)

    # Create user data in DB.
    try:
        user = crud.create_user(db,
                                google_id=user_info['id'],
                                email=user_info['email'],
                                first_name=user_info['given_name'],
                                last_name=user_info['family_name'],
                                thumbnail_url=user_info['picture'])

    except errors.DBError:
        user = crud.read_user(db, google_id=user_info['id'])

    return RedirectResponse(f'/api/auth/generate_token?user_id={user.user_id}')


# TODO: Should be tested.
@router.put('/user/update/{user_id}', tags=['user'])
@router.get('/user/update/{user_id}', tags=['user'])
async def update_user(user_id: str, first_name: str, last_name: str, email: str,
                      db: Session = Depends(database.get_db)):
    try:
        user = crud.update_user(db,
                                user_id=user_id,
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


# TODO: Should be tested.
@router.delete('/user/delete/{user_id}', tags=['user'])
@router.get('/user/delete/{user_id}', tags=['user'])
async def delete_user(user_id: str, db: Session = Depends(database.get_db)):
    try:
        crud.delete_user(db, user_id)
        return {
            'success': True,
            'message': 'User Deleted.'
        }
    except ValueError as e:
        return {
            'success': False,
            'message': e.__repr__()
        }


@router.get('/auth/generate_token', tags=['auth'])
async def generate_token(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.read_user(db, user_id=user_id)

    # Encoding with json.
    jsonized_user_info = jsonable_encoder(user)

    # Issue token
    token: authentication.Token = authentication.generate_token(jsonized_user_info)

    response = RedirectResponse(f'/user/{user.user_id}')

    # Save access_token and refresh_token to cookie.
    response.set_cookie(key='access_token', value=token.access_token, secure=True)
    response.set_cookie(key='refresh_token', value=token.refresh_token, secure=True)

    # Save refresh_token to database.
    try:
        crud.update_user(db,
                         user_id=user_id,
                         email=user.email,
                         first_name=user.first_name,
                         last_name=user.last_name,
                         refresh_token=token.refresh_token)
    except errors.DBError as e:
        print(f'generate token: {e.__repr__()}')
        return {
            'success': False,
            'message': e.__str__()
        }

    return response


@router.get('/auth/update_access_token', tags=['auth'])
async def update_access_token(user_id: str | None = None, refresh_token: str = Cookie(...),
                              db: Session = Depends(database.get_db),
                              callback_uri: str | None = None):
    try:
        authentication.try_is_valid_token('', refresh_token)

        user = crud.read_user(db, user_id=user_id, refresh_token=refresh_token)
    except HTTPException as e:
        # When refresh_token is expired too.
        return {
            'success': False,
            'message': e.detail
        }
    except errors.DBError as e:
        # When no user in database.
        return {
            'success': False,
            'message': e.detail
        }

    # Encoding with json.
    jsonized_user_info = jsonable_encoder(user)

    # Issue token
    token: authentication.Token = authentication.generate_token(jsonized_user_info, update_access_token=True)

    if callback_uri is None:
        response = JSONResponse(content={})
        response.body = {
            'success': True,
            'token_info': {
                'access_token': token.access_token,
                'refresh_token': token.refresh_token
            }
        }
    else:
        response = RedirectResponse(callback_uri)

    # Save access_token to cookie.
    response.set_cookie(key='access_token', value=token.access_token, secure=True)
    return response


@router.get('/auth/revoke_token', tags=['auth'])
async def revoke_token(callback_uri: str | None = None, refresh_token: str = Cookie(...),
                       db: Session = Depends(database.get_db)):
    """
    Remove tokens in cookie and database. After that, Redirect to home.

    :param refresh_token:
    :param db:
    :return:
    """

    response = RedirectResponse('/') if callback_uri is None else RedirectResponse(callback_uri)

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
