from django.db import models

from .product import Product


class Order(models.Model):
    user_name = models.CharField(max_length=50, default="Anonymous")
    user_email = models.EmailField(max_length=50, default="")
    user_phone = models.CharField(max_length=50, default="")
    user_address = models.CharField(max_length=50, default="")
    user_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, verbose_name="Price"
    )

    def __str__(self):
        return f"{self.user_name} - {self.created_at}"

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.order_items.all())

    def save(self, *args, **kwargs):
        self.total_price = self.get_total_price()
        super().save(*args, **kwargs)
