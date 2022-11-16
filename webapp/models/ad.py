from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500)
    href = models.TextField()

    def __str__(self):
        return self.name
