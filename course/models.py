from django.db import models
from django.contrib.auth.models import User
from school.models import School
from datetime import datetime

# Create your models here.
class Course(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    description = models.TextField(default="")
    status = models.IntegerField(default=True)

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,default=None)
    date_creation = models.DateField(default=datetime.now())

class MaterialCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,default=None)
    title = models.TextField(default="")
    content = models.TextField(default="")
    date_creation = models.DateField(default=datetime.now())

class SchoolCourse(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE,default=None)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,default=None)

