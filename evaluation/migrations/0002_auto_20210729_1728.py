# Generated by Django 3.2.5 on 2021-07-29 22:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='status',
        ),
        migrations.RemoveField(
            model_name='userevaluation',
            name='date',
        ),
        migrations.AddField(
            model_name='questionevaluation',
            name='evaluation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='evaluation.evaluation'),
        ),
        migrations.AddField(
            model_name='userevaluation',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2021, 7, 29, 17, 28, 23, 515411)),
        ),
        migrations.AddField(
            model_name='userevaluation',
            name='evaluation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='evaluation.evaluation'),
        ),
        migrations.AddField(
            model_name='userevaluation',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userevaluation',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='questionevaluation',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='questionevaluation',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]