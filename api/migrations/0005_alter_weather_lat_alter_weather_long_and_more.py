# Generated by Django 4.0.3 on 2022-03-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_weather_lat_alter_weather_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='lat',
            field=models.TextField(max_length=25),
        ),
        migrations.AlterField(
            model_name='weather',
            name='long',
            field=models.TextField(max_length=25),
        ),
        migrations.AlterField(
            model_name='weather',
            name='name',
            field=models.TextField(max_length=25),
        ),
    ]
