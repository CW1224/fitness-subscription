# Generated by Django 3.2.19 on 2023-07-05 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
