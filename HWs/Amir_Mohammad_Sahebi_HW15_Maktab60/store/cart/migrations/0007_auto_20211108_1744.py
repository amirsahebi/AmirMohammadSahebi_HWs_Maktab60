# Generated by Django 3.2.9 on 2021-11-08 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211107_1944'),
        ('cart', '0006_auto_20211108_1731'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='cartproduct',
            name='unique_product_cart',
        ),
        migrations.AlterUniqueTogether(
            name='cartproduct',
            unique_together={('cart', 'product')},
        ),
    ]
