from django.db import models


class ErrorStatus(models.Model):
    traceback = models.TextField()
    status_code = models.IntegerField()
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    user_agent = models.TextField()
    ip_address = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Error Statuses'

    def __str__(self):
        return f'{self.status_code} {self.path}'
