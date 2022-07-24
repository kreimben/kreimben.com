from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField(default='')
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title
