# Generated by Django 4.2.5 on 2023-10-16 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
