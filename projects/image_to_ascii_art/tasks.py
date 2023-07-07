from projects.image_to_ascii_art.ascii import get_gray_image_from_s3, convert_to_ascii
from projects.image_to_ascii_art.models import UserUploadedImage, ImageConvertingResult


def draw_ascii_art(pk: int, is_public: bool):
    try:
        user_uploaded_image = UserUploadedImage.objects.get(pk=pk)
    except UserUploadedImage.DoesNotExist:
        return
    key = user_uploaded_image.image.name
    image_object = get_gray_image_from_s3(key)
    ascii_art = convert_to_ascii(image_object)
    ImageConvertingResult.objects.create(
        upload_image=user_uploaded_image,
        compress_level=0,
        is_public=is_public,
        result=ascii_art
    )
