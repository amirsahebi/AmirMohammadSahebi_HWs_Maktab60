# Generated by Django 3.2.9 on 2021-11-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211107_1944'),
        ('cart', '0003_alter_cart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='product.product'),
        ),
    ]