from database.instagram import Instagram
import requests
import shutil
import os


def save_photoes():
    insta = Instagram()
    urls = insta.get_photo_url()
    print(urls)

    for url in urls:
        res = requests.get(url)
        if res.status_code == 200:
            res.raw.decode_content = True
            file_name = url.split("/")[-1].split("?")[0]
            name = r"{}".format(os.getcwd()+"/images/"+file_name)
            with open(name, 'rb+') as f:
                shutil.copyfileobj(res.raw, f)

            print("Image successfully downloaded: ", file_name)
        else:
            print("Image could not be retreived.")


def update_photoes():
    os.removedirs("./images")
    save_photoes()


def get_photoes():
    try:
        with open(os.getcwd()+"/images/*", 'r') as f:
            print(f.readlines())
    except FileNotFoundError:
        print("File not accessible")
