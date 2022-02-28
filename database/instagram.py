import requests


class Instagram:

    def __init__(self):
        with open("./.instagram_token", encoding="utf-8") as f:
            self.__INSTAGRAM_TOKEN = f.readline()

    def __get_user_media(self):

        # caption(hashtag)
        fields = "id"
        url = "https://graph.instagram.com/me/media?fields={}&access_token={}".format(fields, self.__INSTAGRAM_TOKEN)
        result = requests.get(url=url)
        # print(url)
        # print("get user media result: ", result.json())

        return result.json()

    def __get_representative_media_id(self, media_id: str):

        # timestamp
        fields = "id"
        url = "https://graph.instagram.com/{}?fields={}&access_token={}".format(media_id,
                                                                                fields,
                                                                                self.__INSTAGRAM_TOKEN)
        result = requests.get(url=url)
        # print("get_representative_media_id result: ", result.json())

        return result.json()["id"]

    def __get_media_children(self, child_id: str):

        # timestamp
        fields = "id,media_url"
        url = "https://graph.instagram.com/{}/children?fields={}&access_token={}".format(child_id,
                                                                                         fields,
                                                                                         self.__INSTAGRAM_TOKEN)
        result = requests.get(url=url)
        # print("child result: ", result.json())

        return result.json()

    # Use this method ONLY!!!
    def get_photo_url(self) -> [str]:
        media = self.__get_user_media()
        urls = []
        for e in media["data"]:
            e_id = self.__get_representative_media_id(e["id"])
            datas = self.__get_media_children(e_id)["data"]
            for data in datas:
                # Sprint("data: ", data)
                urls.append(data["media_url"])

        return urls
