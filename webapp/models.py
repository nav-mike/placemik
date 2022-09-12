from django.db import models


class CategoryGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey(
        CategoryGroup, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    image_url = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
