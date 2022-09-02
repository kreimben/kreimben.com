from gettext import ngettext

from django.contrib import admin, messages

from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ["make_published", "make_drafted"]

    list_display = ["title", "category", "status", "created_at", "updated_at"]

    search_fields = ["title", "status", "content"]

    list_filter = ("status", )

    @admin.action(description="Make selected posts published.")
    def make_published(self, request, queryset):
        updated = queryset.update(status="Published")
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
        updated = queryset.update(status="Drafted")
        self.message_user(
            request,
            ngettext(
                "%d story was successfully marked as drafted.",
                "%d stories were successfully marked as drafted.",
                updated,
            ) % updated,
            messages.SUCCESS,
        )
