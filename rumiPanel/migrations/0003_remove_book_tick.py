# Generated by Django 4.2.5 on 2023-09-16 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rumiPanel', '0002_book_tick_delete_booksearch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='tick',
        ),
    ]
