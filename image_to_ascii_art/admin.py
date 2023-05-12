from django.contrib import admin

from image_to_ascii_art.models import UserUploadedImage


@admin.register(UserUploadedImage)
class UserUploadedImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'created_at']
    search_fields = ['id', 'user', 'image']
