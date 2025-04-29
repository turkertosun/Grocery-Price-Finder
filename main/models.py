from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title
