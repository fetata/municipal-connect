from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator



class Report(models.Model):

    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"

    STATUS_CHOICES = [
        (OPEN, "Open"),
        (IN_PROGRESS, "In Progress"),
        (RESOLVED, "Resolved"),
    ]

    title = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(5)]
    )
    description = models.TextField(
        validators=[MinLengthValidator(10)]
    )

    location = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(3)]
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=OPEN,
    )

    contact_name = models.CharField(max_length=50)
    phone_validator = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must contain exactly 10 digits."
    )

    contact_phone = models.CharField(
        max_length=10,
        validators=[phone_validator]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def is_active(self):
        return self.status != self.RESOLVED

    def __str__(self):
        return self.title

    def clean(self):
        if self.status == self.RESOLVED and len(self.description) < 20:
            raise ValidationError(
                "Resolved reports must have a detailed description (at least 20 characters)."
            )


