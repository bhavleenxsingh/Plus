# Generated by Django 5.0.6 on 2024-06-24 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_primem_alter_addm_time_alter_expm_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 24, 13, 45, 25, 819745)),
        ),
        migrations.AlterField(
            model_name='expm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 24, 13, 45, 25, 819745)),
        ),
        migrations.AlterField(
            model_name='mulm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 24, 13, 45, 25, 819745)),
        ),
        migrations.AlterField(
            model_name='primem',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 24, 13, 45, 25, 819745)),
        ),
        migrations.AlterField(
            model_name='quom',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 24, 13, 45, 25, 819745)),
        ),
        migrations.AlterField(
            model_name='remm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 24, 13, 45, 25, 819745)),
        ),
        migrations.AlterField(
            model_name='subm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 24, 13, 45, 25, 819745)),
        ),
    ]
