from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


phone_validator = RegexValidator(
    regex=r"^\d{10}$",
    message="Phone number must contain exactly 10 digits.",
)


class MarketplaceCategory(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(3)],
    )

    def __str__(self):
        return self.name


class MarketplaceItem(models.Model):
    OFFER = "Offer"
    WANTED = "Wanted"

    TYPE_CHOICES = [
        (OFFER, "Offer"),
        (WANTED, "Wanted"),
    ]

    NEW = "New"
    USED = "Used"

    CONDITION_CHOICES = [
        (NEW, "New"),
        (USED, "Used"),
    ]

    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
    )

    description = models.TextField(
        validators=[MinLengthValidator(10)],
    )

    image = models.ImageField(
        upload_to="marketplace/",
        blank=True,
        null=True,
    )

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
    )

    condition = models.CharField(
        max_length=10,
        choices=CONDITION_CHOICES,
    )

    contact_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
    )

    contact_phone = models.CharField(
        max_length=10,
        validators=[phone_validator],
    )

    category = models.ForeignKey(
        MarketplaceCategory,
        on_delete=models.CASCADE,
        related_name="items",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
