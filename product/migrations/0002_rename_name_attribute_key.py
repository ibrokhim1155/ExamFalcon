# Generated by Django 5.1 on 2024-08-18 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='name',
            new_name='key',
        ),
    ]