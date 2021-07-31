from django.db import models

from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    phone = models.IntegerField()
    date_birth = models.DateField()
    status = models.BooleanField(default=True)

class Address(models.Model):
    city = models.CharField(max_length=200,default="")
    province = models.CharField(max_length=200,default="")
    country = models.CharField(max_length=200,default="")
    date_creation = models.DateField(default=datetime.now())