from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
# Create your models here.

class Evaluation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    num_question = models.IntegerField()

class UserEvaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE,default=None)
    date_creation = models.DateField(default=datetime.now())
    status = models.BooleanField(default=True)

class QuestionEvaluation(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=200,default="")
    description = models.TextField(default="")
    alternatives = models.TextField(default="")
    number = models.IntegerField(default=0)
