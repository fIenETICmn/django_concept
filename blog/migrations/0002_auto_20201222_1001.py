# Generated by Django 3.1.4 on 2020-12-22 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Productimage',
        ),
    ]