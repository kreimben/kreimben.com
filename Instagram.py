import requests
from logging import debug, info, error

INSTAGRAM_TOKEN = ""

with open("./.instagram_token", encoding="utf-8") as f:
    INSTAGRAM_TOKEN = f.readline()


def get_user_media():
    global INSTAGRAM_TOKEN

    fields = "id" # caption(hashtag)
    url = "https://graph.instagram.com/me/media?fields={}&access_token={}".format(fields, INSTAGRAM_TOKEN)
    result = requests.get(url=url)
    print(url)
    print("get user media result: ", result.json())

    return result.json()


def get_representative_media_id(media_id: str):
    global INSTAGRAM_TOKEN

    fields = "id" # timestamp
    url = "https://graph.instagram.com/{}?fields={}&access_token={}".format(media_id, fields, INSTAGRAM_TOKEN)
    result = requests.get(url=url)
    debug("get_representative_media_id result: ", result.json())

    return result.json()["id"]


def get_media_children(child_id: str):
    global INSTAGRAM_TOKEN

    fields = "id,media_url" # timestamp
    url = "https://graph.instagram.com/{}/children?fields={}&access_token={}".format(child_id, fields, INSTAGRAM_TOKEN)
    result = requests.get(url=url)
    debug("child result: ", result.json())

    return result.json()


# Use this method ONLY!!!
def get_photo_url():
    media = get_user_media()
    urls = []
    for e in media["data"]:
        e_id = get_representative_media_id(e["id"])
        datas = get_media_children(e_id)["data"]
        for data in datas:
            print("data: ", data)
            urls.append(data["media_url"])