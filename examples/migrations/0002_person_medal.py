# Generated by Django 3.0.2 on 2020-06-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='medal',
            field=models.CharField(blank=True, choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')], max_length=10),
        ),
    ]
