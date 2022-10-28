from django.db import models
from .category_group import CategoryGroup


class Category(models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey(
        CategoryGroup,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="categories",
    )

    def __str__(self):
        return self.name
