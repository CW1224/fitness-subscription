# Generated by Django 3.2.19 on 2023-07-02 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_users_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='users_favorite',
        ),
    ]