from django.contrib import admin

from projects.mnist_classifier.models import MnistClassifierHistory


@admin.register(MnistClassifierHistory)
class MnistClassifierHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'created_at']
    search_fields = ['id', 'ip']
