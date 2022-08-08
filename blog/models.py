from django.db import models
from django_quill.fields import QuillField


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        get_latest_by = '-created_at'
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
    status = models.CharField(max_length=10,
                              choices=(('Drafted', 'drafted'), ('Published', 'published')),
                              default='Drafted')
    content = QuillField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = ['title', '-created_at']
        verbose_name = 'post'
        verbose_name_plural = 'posts'
