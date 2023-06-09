# Generated by Django 3.2.19 on 2023-07-04 20:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_remove_product_users_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
