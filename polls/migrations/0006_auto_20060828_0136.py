# Generated by Django 3.0.2 on 2006-08-27 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20060828_0047'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='QuestionComment',
        ),
    ]
