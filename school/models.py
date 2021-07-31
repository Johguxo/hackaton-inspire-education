from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.
class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    department = models.CharField(max_length=200,default="")
    description = models.TextField(default="")
    salary = models.IntegerField()

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    grade = models.IntegerField()
    description = models.IntegerField()
    skills = models.CharField(max_length=200,default="")

class School(models.Model):
    name = models.CharField(max_length=200,default="")
    description = models.TextField(default="")

class UserSchool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    school = models.ForeignKey(School, on_delete=models.CASCADE,default=None)
    date_creation = models.DateField(default=datetime.now())
    status = models.IntegerField(default=True)


    
