from django.db import models
from django_quill.fields import QuillField


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        get_latest_by = "-created_at"
        verbose_name = "category"
        verbose_name_plural = "categories"


class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
            .select_related('category') \
            .order_by("-created_at") \
            .filter(status__exact='published')


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_DEFAULT,
                                 default=1)
    status = models.CharField(
        max_length=10,
        choices=(("drafted", "Drafted"), ("published", "Published")),
        default="drafted",
    )
    content = QuillField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    published = PublishedPostManager()

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = ["title", "-created_at"]
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['-created_at']


class SubmittedFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='files')
    file = models.FileField()
    download_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def download(self) -> str:
        self.download_count += 1
        self.save()
        return self.file.url

    def __str__(self):
        return f'{self.file.name} ({self.post.title})'

    class Meta:
        get_latest_by = ['-updated_at']
        verbose_name = 'Submitted File'
        verbose_name_plural = 'Submitted Files'


class Downloader(models.Model):
    file = models.ForeignKey(SubmittedFile, on_delete=models.CASCADE, related_name='downloaders')
    ip_address = models.GenericIPAddressField()
    city = models.CharField(max_length=1000, null=True, blank=True)
    country_name = models.CharField(max_length=1000, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    time_zone = models.CharField(max_length=1000, null=True, blank=True)
    download_request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ip_address} ({self.city})'

    class Meta:
        get_latest_by = ['-download_request_time']
        verbose_name = 'Downloader'
        verbose_name_plural = 'Downloaders'
