from typing import Any
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    image_url = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def rating(self) -> int:
        if reviews := self.reviews.all():
            return int(sum(review.rating for review in reviews) / reviews.count())
        return 0
