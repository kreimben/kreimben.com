import json

import requests


def get_secret():
    data = None
    with open('../google_oauth2_secret.json') as f:
        data = json.load(f)
    return data


def get_access_token_from_google(code: str):
    data = get_secret()

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


def get_user_info(access_token: str) -> dict:
    url = f'https://www.googleapis.com/oauth2/v1/userinfo'
    alt = '?alt=json'
    at = f'&access_token={access_token}'
    scope = f'&scope=https://www.googleapis.com/auth/userinfo.profile'

    url += alt + at + scope

    json = requests.get(url).json()

    # print(f'user info: {json}')

    return json
