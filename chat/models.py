from django.db import models


class Chatter(models.Model):
    hashed_value = models.CharField(max_length=8)
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=100, null=True, blank=True)
    region_name = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=1000, null=True, blank=True)
    timezone = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'({self.id}) {self.hashed_value} ({self.ip_address})'


class Chat(models.Model):
    chatter = models.ForeignKey(Chatter, on_delete=models.CASCADE, related_name='chats')
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.message} ({self.chatter})'
