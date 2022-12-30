from django.contrib import admin

from chat.models import Chatter, Chat


@admin.register(Chatter)
class ChatterAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 'country', 'region_name', 'city', 'timezone', 'created_at']
    list_filter = ['country', 'timezone']


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'chatter', 'created_at']
    list_filter = ['chatter']
