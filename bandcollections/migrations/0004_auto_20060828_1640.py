# Generated by Django 3.0.2 on 2006-08-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandcollections', '0003_auto_20060901_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musiciandi',
            name='information',
            field=models.TextField(),
        ),
    ]
