from django.contrib import admin

from .models import Evaluation, UserEvaluation, QuestionEvaluation
# Register your models here.

admin.site.register(Evaluation)
admin.site.register(UserEvaluation)
admin.site.register(QuestionEvaluation)
