# Generated by Django 4.2.5 on 2023-10-20 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0003_remove_advertisement_draft_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='favorites',
        ),
    ]
