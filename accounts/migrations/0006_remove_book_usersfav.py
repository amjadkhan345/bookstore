# Generated by Django 3.0.6 on 2020-05-20 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_book_usersfav'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='usersfav',
        ),
    ]
