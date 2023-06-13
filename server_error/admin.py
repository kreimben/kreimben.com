from django.contrib import admin

from server_error.models import ErrorStatus


@admin.register(ErrorStatus)
class ErrorStatusAdmin(admin.ModelAdmin):
    list_display = ('status_code', 'path', 'method', 'user_agent', 'ip_address', 'created_at')
    search_fields = ('status_code', 'path', 'method', 'user_agent', 'ip_address', 'created_at')
    readonly_fields = ('status_code', 'path', 'method', 'user_agent', 'ip_address', 'created_at')
