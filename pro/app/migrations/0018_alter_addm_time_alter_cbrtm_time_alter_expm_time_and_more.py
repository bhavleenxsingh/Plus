# Generated by Django 5.0.6 on 2024-07-03 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_inchm_alter_addm_time_alter_cbrtm_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 263648)),
        ),
        migrations.AlterField(
            model_name='cbrtm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 263648)),
        ),
        migrations.AlterField(
            model_name='expm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 263648)),
        ),
        migrations.AlterField(
            model_name='facm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 279265)),
        ),
        migrations.AlterField(
            model_name='fibm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 263648)),
        ),
        migrations.AlterField(
            model_name='inchm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 279265)),
        ),
        migrations.AlterField(
            model_name='milem',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 279265)),
        ),
        migrations.AlterField(
            model_name='mulm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 263648)),
        ),
        migrations.AlterField(
            model_name='otpm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 263648)),
        ),
        migrations.AlterField(
            model_name='primem',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 263648)),
        ),
        migrations.AlterField(
            model_name='quom',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 263648)),
        ),
        migrations.AlterField(
            model_name='remm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 263648)),
        ),
        migrations.AlterField(
            model_name='sqrtm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 263648)),
        ),
        migrations.AlterField(
            model_name='subm',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 46, 16, 263648)),
        ),
    ]
