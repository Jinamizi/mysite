# Generated by Django 3.0.2 on 2006-08-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20060828_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporter',
            name='first_name',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='last_name',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='sirname',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
    ]
