import os.path
import firebase_admin
from firebase_admin import credentials, firestore

base_app: firebase_admin.App


def init_firebase_admin_sdk():
    global base_app

    cred = credentials.Certificate(_get_file_path("./kreimben-com-firebase-adminsdk-37j58-dd6f28039b.json"))
    base_app = firebase_admin.initialize_app(cred, {
        'databaseURL': ''
    })


def read_posts():
    c = _get_client()
    db_ref = c.collection('post')
    docs = db_ref.stream()
    results = []
    for doc in docs:
        print("{} => {}".format(doc.id, doc.to_dict()))
        results.append(doc.to_dict())

    return results


def write_post(param: dict):
    c = _get_client()
    c.collection('post').add(param)


def _get_client():
    return firestore.client()


def _get_file_path(path: str):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, path)