from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=100)
    fabric_type = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.color})"

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

