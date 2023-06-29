from django.db import models


class Sort(models.Model):
    name = models.CharField(max_length=100)
    time_complexity = models.CharField(max_length=100)
    space_complexity = models.CharField(max_length=100)
    best_case = models.CharField(max_length=100)
    worst_case = models.CharField(max_length=100)
    average_case = models.CharField(max_length=100)
    code = models.TextField()

    class META:
        ordering = ['name']
