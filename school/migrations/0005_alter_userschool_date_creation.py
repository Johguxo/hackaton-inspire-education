# Generated by Django 3.2.5 on 2021-07-31 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_userschool_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userschool',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2021, 7, 31, 2, 1, 35, 945757)),
        ),
    ]
