from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .product import Product


class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    user_name = models.CharField(max_length=50, default="Anonymous")
    city = models.CharField(max_length=50, default="")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="reviews",
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
