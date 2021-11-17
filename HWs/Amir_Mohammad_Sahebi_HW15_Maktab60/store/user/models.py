from django.db import models
from product.models import *

# Create your models here.

class User(models.Model):
    gender=(
        ('Male','male'),
        ('Female','female'),
        ('Undefind','undefind')
    )
    name=models.CharField(max_length=255)
    natinal_code=models.PositiveIntegerField()
    address=models.CharField(max_length=255)
    phone=models.PositiveIntegerField()
    sex=models.CharField(max_length=8,choices=gender)

    def __str__(self):
        return self.name


class Seller(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key= True)
    product=models.ForeignKey("cart.Cart",on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name