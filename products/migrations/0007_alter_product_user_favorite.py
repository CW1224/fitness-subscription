# Generated by Django 3.2.19 on 2023-07-04 20:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_product_user_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user_favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
