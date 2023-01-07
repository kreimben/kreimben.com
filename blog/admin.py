from gettext import ngettext

from django.contrib import admin, messages

from .models import Category, Post, SubmittedFile, Downloader


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ["make_published", "make_drafted"]
    list_display = ["id", "title", 'view_count', "category", "status", "created_at", "updated_at"]
    readonly_fields = ['view_count']
    search_fields = ["title", "status", "content"]
    list_filter = ["status"]
    show_full_result_count = True

    def get_queryset(self, request):
        qs = self.model.objects.get_queryset()
        return qs

    @admin.action(description="Make selected posts published.")
    def make_published(self, request, queryset):
        updated = queryset.update(status="published")
        self.message_user(
            request,
            ngettext(
                "%d story was successfully marked as published.",
                "%d stories were successfully marked as published.",
                updated,
            ) % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Make selected posts drafted.")
    def make_drafted(self, request, queryset):
        updated = queryset.update(status="drafted")
        self.message_user(
            request,
            ngettext(
                "%d story was successfully marked as drafted.",
                "%d stories were successfully marked as drafted.",
                updated,
            ) % updated,
            messages.SUCCESS,
        )


@admin.register(SubmittedFile)
class SubmittedFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'download_count', 'post', 'created_at', 'updated_at']
    search_fields = ['file_name', 'file_url', 'post']


@admin.register(Downloader)
class DownloaderAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'city', 'country_name', 'download_request_time']
    search_fields = list_display
