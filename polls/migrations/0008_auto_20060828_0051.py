# Generated by Django 3.0.2 on 2006-08-27 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20060828_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('date_joined', models.DateTimeField(verbose_name='date joined')),
            ],
            options={
                'ordering': ['-date_joined', 'username'],
            },
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'ordering': ['-votes']},
        ),
        migrations.AlterModelOptions(
            name='commentcomment',
            options={'ordering': ['-date_commented', 'likes']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='questioncomment',
            options={'ordering': ['-date_commented', 'likes']},
        ),
    ]
