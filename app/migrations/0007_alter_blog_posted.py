# Generated by Django 5.0 on 2023-12-08 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_blog_author_remove_blog_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 8, 13, 1, 56, 463752), verbose_name='Опубликована'),
        ),
    ]
