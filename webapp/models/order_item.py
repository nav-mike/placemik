from django.db import models

from .product import Product
from .order import Order


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="order_items",
    )
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, verbose_name="Price"
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name="order_items",
    )

    def __str__(self):
        return f"{self.product.name} - {self.quantity} шт."

    def get_total_price(self):
        return self.quantity * self.price

    def save(self, *args, **kwargs):
        self.price = self.product.price
        super().save(*args, **kwargs)
