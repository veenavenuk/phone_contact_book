# Generated by Django 4.1.2 on 2022-10-13 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcb_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone_book',
            old_name='Id',
            new_name='id',
        ),
    ]
