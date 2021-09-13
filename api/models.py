from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=11)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    category = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name
