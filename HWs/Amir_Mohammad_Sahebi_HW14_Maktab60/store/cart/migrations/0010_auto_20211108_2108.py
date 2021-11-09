# Generated by Django 3.2.9 on 2021-11-08 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211107_1944'),
        ('cart', '0009_alter_cartproduct_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='CartProduct',
        ),
        migrations.AddField(
            model_name='favoriteitem',
            name='favorite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.favorite'),
        ),
        migrations.AddField(
            model_name='favoriteitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AlterUniqueTogether(
            name='favoriteitem',
            unique_together={('favorite', 'product')},
        ),
    ]
