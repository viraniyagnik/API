# Generated by Django 4.0.3 on 2022-05-26 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_custom_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='phone',
            field=models.CharField(default=9876543210, max_length=10),
        ),
    ]
