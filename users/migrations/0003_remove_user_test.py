# Generated by Django 4.2.13 on 2024-07-26 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='test',
        ),
    ]
