# Generated by Django 4.2.13 on 2024-07-14 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='prise',
            new_name='price',
        ),
    ]
