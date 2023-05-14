from django.contrib import admin

from image_to_ascii_art.models import UserUploadedImage, ImageConvertingResult


@admin.register(UserUploadedImage)
class UserUploadedImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'created_at']
    search_fields = ['id', 'user', 'image']


@admin.register(ImageConvertingResult)
class ImageConvertingResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'upload_image', 'compress_level', 'created_at']
    list_filter = ['compress_level']
    search_fields = ['id', 'upload_image', 'result']
