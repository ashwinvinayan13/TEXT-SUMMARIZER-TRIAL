from django.db import models

# Create your models here.

class CategoryDB(models.Model):
    Name = models.CharField(max_length=200, null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="Images", null=True, blank=True)


class ProductDB(models.Model):
    Name = models.CharField(max_length=200, null=True, blank=True)
    Product = models.CharField(max_length=200, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=200, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="Image", null=True, blank=True)


