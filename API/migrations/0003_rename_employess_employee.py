# Generated by Django 4.2 on 2024-04-25 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_employess'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employess',
            new_name='Employee',
        ),
    ]