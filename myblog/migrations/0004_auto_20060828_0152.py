# Generated by Django 3.0.2 on 2006-08-27 22:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20200622_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2006, 8, 27, 22, 52, 7, 329101, tzinfo=utc)),
        ),
    ]
