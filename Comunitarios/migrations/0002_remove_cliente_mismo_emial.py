# Generated by Django 5.0 on 2023-12-24 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comunitarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='mismo_emial',
        ),
    ]
