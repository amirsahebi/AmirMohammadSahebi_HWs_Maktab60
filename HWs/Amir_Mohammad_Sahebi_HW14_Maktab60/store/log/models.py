from django.db import models
from user.models import *
from cart.models import *
# Create your models here.

class Email_log(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    email_sent_status = models.BooleanField(default=False)
