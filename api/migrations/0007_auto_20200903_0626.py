# Generated by Django 3.1 on 2020-09-03 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200903_0524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='user1',
            field=models.CharField(default='nun', max_length=300),
        ),
    ]
