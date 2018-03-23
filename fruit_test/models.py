from django.db import models


class Fruits(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
