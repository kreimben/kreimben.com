from database.instagram import Instagram
import requests, shutil, os, glob


def save_photos():
    insta = Instagram()
    urls = insta.get_photo_url()
    print(urls)

    for url in urls:
        res = requests.get(url, stream = True)
        if res.status_code == 200:
            res.raw.decode_content = True
            file_name = url.split("/")[-1].split("?")[0]
            name = r'{}'.format(os.getcwd()+"/app/database/images/"+file_name)
            with open(name, 'wb+') as f:
                shutil.copyfileobj(res.raw, f)
                # f.write(response.content)

            print("Image successfully downloaded: ", file_name)
        else:
            print("Image could not be retreived.")


def update_photos() -> [str]:
    path = r'{}/app/database/images'.format(os.getcwd())
    # print(path)
    files = os.listdir(path)
    try:
        for file in files:
            os.unlink(file)
    except FileNotFoundError:
        pass
    save_photos()
    return get_photos()


def get_photos() -> [str]:
    urls: [str] = []
    try:
        path = r'{}'.format(os.getcwd()+"/app/database/images/*")
        for file in glob.glob(path):
            # print(file)
            urls.append(file)

    except FileNotFoundError:
        print("File not accessible")

    return urls
