from django.db import models


# Create your models here.


class Category(models.Model):

    parent = models.ForeignKey('self', default=None, null=True, blank=True, related_name='nested_category',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255)
    year = models.DateField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey("user.User",on_delete=models.CASCADE)
    product = models.ForeignKey("product.Product",on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)





