# Generated by Django 4.0.3 on 2022-05-26 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_geolocation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='geolocation',
            name='Latitude',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='geolocation',
            name='Longitude',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=12),
        ),
    ]