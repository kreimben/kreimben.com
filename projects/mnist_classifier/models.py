from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class MnistClassifierHistory(models.Model):
    ip = models.GenericIPAddressField()
    expected_number = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9)],
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
