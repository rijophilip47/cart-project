from django.db import models

# Create your models here.

class Category(models.Model):
    name         = models.CharField(max_length=15)
    description  = models.CharField(max_length=40)
    image        = models.ImageField(upload_to='sample',default='null.jpg')
    

class Product(models.Model):
    name         = models.CharField(max_length=15)
    description  = models.CharField(max_length=40)
    price        = models.IntegerField()
    image        = models.ImageField(upload_to='sample',default='null.jpg')
    category     = models.CharField(max_length=15)