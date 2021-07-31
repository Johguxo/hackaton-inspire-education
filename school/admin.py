from django.contrib import admin

from .models import Teacher, Student, UserSchool,School
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(UserSchool)
admin.site.register(School)
