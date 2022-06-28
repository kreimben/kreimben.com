import os

from dotenv import load_dotenv

load_dotenv()


def get_secret_key() -> str:
    return os.environ.get('OAUTH2_SECRET_KEY')
