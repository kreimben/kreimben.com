from fastapi import APIRouter, Request, Depends, HTTPException, Cookie
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse, JSONResponse
from sqlalchemy.orm import Session

import app.model.crud as crud
import app.model.database as database
import app.utils.authentication as authentication
import app.utils.errors as errors
import app.utils.google_auth as ga
from app.utils.errors import DBError

router = APIRouter(prefix='/api', tags=['api'])


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
    response = RedirectResponse('/')

    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')

    return response


@router.get('/redirect')
async def redirect(code: str, db: Session = Depends(database.get_db)):
    data = ga.get_access_token_from_google(code)
    google_access_token = data['access_token']

    user_info = ga.get_user_info(google_access_token)
    google_id = user_info['id']

    try:
        user = crud.read_user(db, google_id=google_id)
        return RedirectResponse(f'/user/{user.user_id}')
    except DBError as e:
        print(f'DBError in read_user: {e.__repr__()}')
        return RedirectResponse(f'/api/user/create?google_access_token={google_access_token}')


@router.post('/user/create', status_code=201)
@router.get('/user/create', status_code=201)
async def create_user(google_access_token: str, db: Session = Depends(database.get_db)):
    user_info = ga.get_user_info(google_access_token)

    # try:

    # Create user data in DB.
    user = crud.create_user(db,
                            google_id=user_info['id'],
                            email=user_info['email'],
                            first_name=user_info['given_name'],
                            last_name=user_info['family_name'],
                            thumbnail_url=user_info['picture'])

    # Encoding with json.
    jsonized_user_info = jsonable_encoder(user)
    # print(f'jsonized_user_info: {jsonized_user_info}')

    # Issue token
    token: authentication.Token = authentication.generate_token(jsonized_user_info)

    response = RedirectResponse(f'/user/{user.user_id}')

    # Save access_token and refresh_token to cookie.
    response.set_cookie(key='access_token', value=token.access_token, secure=True)
    response.set_cookie(key='refresh_token', value=token.refresh_token, secure=True)

    return response

    # except errors.DBError as e:
    #     print(f'value error in create_user function: {e.__repr__()}')
    #     return {
    #         'success': False,
    #         'message': e.__str__()
    #     }


# TODO: Should be tested.
@router.get('/auth/update_access_token')
async def update_access_token(user_id: str, refresh_token: str = Cookie(...),
                              db: Session = Depends(database.get_db),
                              callback_uri: str | None = None):
    try:
        authentication.is_valid_token('', refresh_token)

        user = crud.read_user(db, user_id)
    except HTTPException as e:
        return {
            'success': False,
            'message': e.detail
        }
    except errors.DBError as e:
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


@router.get('/auth/revoke_token/{user_id}')
async def revoke_token(request: Request, user_id: str, db: Session = Depends(database.get_db)):
    items = []

    for _ in range(request.cookies.__len__()):
        items.append(request.cookies.popitem())

    response = JSONResponse(content={
        'success': True,
        'items': items
    })

    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')

    return response


# @router.get('/user/{user_id}')
# async def get_user_info(user_id: str, access_token: str = Cookie(), refresh_token: str = Cookie(),
#                         db: Session = Depends(database.get_db)):
#     try:
#         # Validate given token.
#         if not authentication.is_valid_token(access_token, refresh_token):
#             # access_token is expired.
#             await update_access_token(user_id, db=db)
#
#         # Check user from db.
#         user = crud.read_user(db, user_id=user_id)
#         value = {
#             'success': True,
#             'user': user
#         }
#         return value
#     except ValueError as e:
#         # print(f'no such user in /user/google_id fucntion: {e.__repr__()}')
#         return {
#             'success': False,
#             'message': e.__str__()
#         }
#     except HTTPException as e:
#         return {
#             'success': False,
#             'message': e.detail
#         }
#     except PyJWTError as e:
#         # Refresh Token Expired.
#         # Delete tokens and re-login.
#         response = RedirectResponse(f'/login')
#         response.delete_cookie('access_token')
#         response.delete_cookie('refresh_token')
#         return response


# TODO: Should be tested.
@router.put('/user/update/{google_id}')
@router.get('/user/update/{google_id}')
async def update_user(google_id: str, first_name: str, last_name: str, email: str,
                      db: Session = Depends(database.get_db)):
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


# TODO: Should be tested.
@router.delete('/user/delete/{google_id}')
@router.get('/user/delete/{google_id}')
async def delete_user(google_id: str, db: Session = Depends(database.get_db)):
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


# TODO: Should be tested.
@router.post('/authorization/create/{name}')
@router.get('/authorization/create/{name}')
async def create_authorization(name: str, db: Session = Depends(database.get_db)):
    try:
        crud.create_authorization(db, name=name)
        return JSONResponse(status_code=201, content={
            'success': True,
            'message': 'Authorization Created.',
            'name': name
        })
    except ValueError as e:
        return {
            'success': False,
            'message': e.__repr__()
        }
