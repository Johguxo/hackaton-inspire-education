# Generated by Django 3.2.5 on 2021-07-31 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialcourse',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2021, 7, 31, 2, 1, 35, 947757)),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2021, 7, 31, 2, 1, 35, 947257)),
        ),
    ]
