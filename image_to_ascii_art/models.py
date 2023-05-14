from django.conf import settings
from django.db import models


def user_uploaded_image_path(instance, filename):
    return f'image_to_ascii_art/user_uploaded_image/{instance.user.id}/{filename}'


class UserUploadedImage(models.Model):
    """
    user uploaded original image
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_uploaded_image_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.image.name.split("/")[-1]} (uploaded by {self.user.username})'

    class Meta:
        get_latest_by = ['-updated_at']
        verbose_name = 'User Uploaded Image'
        verbose_name_plural = 'User Uploaded Images'


class ImageConvertingResult(models.Model):
    upload_image = models.ForeignKey(UserUploadedImage, on_delete=models.CASCADE)
    compress_level = models.PositiveSmallIntegerField()
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # exactly converted at

    def __str__(self):
        return f'{self.upload_image.user.username}'

    class Meta:
        get_latest_by = ['-created_at']
        verbose_name = 'Image Converting Result'
        verbose_name_plural = 'Image Converting Results'
