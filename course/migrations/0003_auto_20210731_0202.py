# Generated by Django 3.2.5 on 2021-07-31 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20210731_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialcourse',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2021, 7, 31, 2, 2, 39, 542594)),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2021, 7, 31, 2, 2, 39, 542097)),
        ),
    ]