# Generated by Django 4.0.3 on 2022-05-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_id_custom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocation',
            name='Name',
            field=models.CharField(default='none', max_length=200),
        ),
    ]