from django.db import models
from adminapp.models import *

# Create your models here.
class Register(models.Model):
    username     = models.CharField(max_length=15)
    phone        = models.IntegerField()
    email        = models.EmailField()
    password     = models.CharField(max_length=40)
    
class ContactDB(models.Model):
    name = models.CharField(max_length=15)
    email=models.EmailField()
    comment=models.CharField(max_length=255)
    
class CartDB(models.Model):
    user_id = models.ForeignKey(Register,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.IntegerField()
    status = models.IntegerField(default=0)
    
class CheckoutDB(models.Model):
    user_id = models.ForeignKey(Register,models.CASCADE)
    cart_id = models.ForeignKey(CartDB,models.CASCADE)
    address = models.CharField(max_length=255)
    city    = models.CharField(max_length=15)
    state   = models.CharField(max_length=15,default="")
    country = models.CharField(max_length=15)
    postal_zip=models.CharField(max_length=15)
    

    
    
    