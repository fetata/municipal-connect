from django.core.validators import MinLengthValidator
from django.db import models


class Announcement(models.Model):
    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)],
    )

    content = models.TextField(
        validators=[MinLengthValidator(20)],
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
