# Generated by Django 3.0.2 on 2020-06-22 14:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20200612_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 14, 14, 35, 765625, tzinfo=utc)),
        ),
    ]
