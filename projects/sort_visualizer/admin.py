from django.contrib import admin

from projects.sort_visualizer.models import Sort


@admin.register(Sort)
class SortAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_complexity', 'space_complexity', 'best_case', 'worst_case', 'average_case', 'code')
    list_filter = ('name', 'time_complexity', 'space_complexity', 'best_case', 'worst_case', 'average_case', 'code')
    search_fields = ('name', 'time_complexity', 'space_complexity', 'best_case', 'worst_case', 'average_case', 'code')
    ordering = ['name']
