from django.db import models
from enum import Enum


class NutritionalType(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name + '(' + self.unit + ')'

class Product(models.Model):
    STATUS_CHOICES = (
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE')
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default='ACTIVE',
    )

    def __str__(self):
        return self.name


class NutritionalValues(models.Model):
    product = models.ForeignKey(Product, related_name='nutritionalvalues', on_delete=models.CASCADE)
    nutritional_type = models.ForeignKey(NutritionalType, related_name='ntype', on_delete=models.CASCADE)
    nutritional_value = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nutritional_type.name + '(' + self.nutritional_type.unit + '): ' + str(self.nutritional_value) + ' -> ' +self.product.name
