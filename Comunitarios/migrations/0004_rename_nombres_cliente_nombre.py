# Generated by Django 5.0 on 2023-12-26 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comunitarios', '0003_cliente_nombres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='nombres',
            new_name='nombre',
        ),
    ]
