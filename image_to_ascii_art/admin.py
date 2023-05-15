from django.contrib import admin

from image_to_ascii_art.models import UserUploadedImage, ImageConvertingResult


@admin.register(UserUploadedImage)
class UserUploadedImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'created_at']
    search_fields = ['id', 'user', 'image']


@admin.register(ImageConvertingResult)
class ImageConvertingResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'upload_image', 'is_public', 'compress_level', 'created_at']
    readonly_fields = ['image_tag']
    list_filter = ['compress_level', 'upload_image__user']
    list_select_related = ['upload_image']
    search_fields = ['id', 'upload_image__image', 'result']
    actions = ['make_public', 'make_private']

    @admin.action(description='Make public')
    def make_public(self, request, queryset):
        queryset.update(is_public=True)
        self.message_user(request, 'Successfully made public', level='SUCCESS')

    @admin.action(description='Make private')
    def make_private(self, request, queryset):
        queryset.update(is_public=False)
        self.message_user(request, 'Successfully made private', level='SUCCESS')
