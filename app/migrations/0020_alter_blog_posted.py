# Generated by Django 5.0 on 2023-12-08 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 8, 15, 43, 18, 316268), verbose_name='Опубликована'),
        ),
    ]
