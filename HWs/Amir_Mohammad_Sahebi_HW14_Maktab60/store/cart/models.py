
from enum import unique
from django.db import models
from user.models import *
from product.models import *
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    
    def __str__(self):
        return self.user.name

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

       

    def __str__(self):
        return self.product.name

    

class Favorite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.name
    

class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['favorite','product']

    def __str__(self):
        return self.product.name
