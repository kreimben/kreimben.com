from django.db import models


class Sort(models.Model):
    name = models.CharField(max_length=100)
    time_complexity = models.CharField(max_length=100)
    space_complexity = models.CharField(max_length=100)
    best_case = models.CharField(max_length=100)
    worst_case = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    extra_info = models.TextField(null=True, blank=True)

    class META:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
