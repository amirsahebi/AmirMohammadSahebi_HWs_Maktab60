# در اپ اصلی این قطعه جایگذاری شده است
# منیجر در واقع رابط ما با دیتابیس است و میتوانیم با استفاده از آن کویری دلخواه خود را ایجاد میکنیم
from django.db import models


class AvailablesManager(models.manager):
    def get_queryset(self):
        return super(AvailablesManager, self).get_queryset().filter(status="Available")

class UnavailablesManager(models.manager):
    def get_queryset(self):
        return super(UnavailablesManager, self).get_queryset().filter(status="Unavailable")


class Product(models.Model):
    statuses=(
        ("Available","available"),
        ("Unavailable","unavailble")
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255)
    year = models.DateField()
    country = models.CharField(max_length=255)
    status = models.CharField(choices=statuses)


    available_products = AvailablesManager()
    unavailable_products = UnavailablesManager()

    def __str__(self):
        return self.name




    





