import io
import os

import PIL.Image as PILI
import boto3

char_set = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.'


def get_gray_image_from_s3(key: str):
    s3 = boto3.client(
        's3',
        region_name=os.getenv('AWS_S3_CUSTOM_DOMAIN').split('.')[1],
        endpoint_url='https://' + os.getenv('AWS_S3_CUSTOM_DOMAIN'),
        aws_access_key_id=os.getenv('AWS_S3_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_S3_SECRET_ACCESS_KEY'),
    )
    output = io.BytesIO()
    s3.download_fileobj(Bucket=os.getenv('AWS_STORAGE_BUCKET_NAME'), Key=key, Fileobj=output)
    output.seek(0)
    image = __get_gray_image(__get_image(output))
    output.close()
    s3.close()
    return image


def __get_image(image_name):
    """
    :param image_name - real file name or file-like object.
    """
    return PILI.open(image_name)


def __get_gray_image(image):
    return image.convert("L")


def convert_to_ascii(image, compress_ratio: int = 3) -> str:
    width, height = image.size
    ratio = height / width
    height = int(width * ratio * 0.5)
    image = image.resize((width, height), PILI.LANCZOS)
    res = ''
    N = len(char_set)
    for i in range(0, height, compress_ratio):
        for j in range(0, width, compress_ratio):
            pixel = image.getpixel((j, i))
            res += char_set[int(pixel / (256 / N))]
        res += '\n'
    return res
