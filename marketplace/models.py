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
    class Type(models.TextChoices):
        OFFER = "Offer", "Offer"
        WANTED = "Wanted", "Wanted"
        GIVEAWAY = "Giveaway", "Giveaway"

    class Condition(models.TextChoices):
        NEW = "New", "New"
        USED = "Used", "Used"

    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
    )

    description = models.TextField(
        validators=[MinLengthValidator(10)],
    )



    type = models.CharField(
        max_length=10,
        choices=Type.choices,
    )

    condition = models.CharField(
        max_length=20,
        choices=Condition.choices,
        blank=True,
        null=True,
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

    image = models.ImageField(
        upload_to="marketplace/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
