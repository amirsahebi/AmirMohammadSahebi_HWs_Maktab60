# Generated by Django 3.2.9 on 2021-11-08 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211107_1944'),
        ('cart', '0008_alter_cartproduct_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartproduct',
            unique_together={('cart', 'product')},
        ),
    ]
