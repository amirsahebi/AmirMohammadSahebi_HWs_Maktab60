# Generated by Django 3.2.9 on 2021-11-08 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_price'),
        ('user', '0003_alter_seller_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='product',
            field=models.ManyToManyField(to='product.Product'),
        ),
    ]
