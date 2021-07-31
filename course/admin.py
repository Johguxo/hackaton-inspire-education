from course.models import MaterialCourse, SchoolCourse, UserCourse,Course
from django.contrib import admin

# Register your models here.
admin.site.register(Course)
admin.site.register(UserCourse)
admin.site.register(SchoolCourse)
admin.site.register(MaterialCourse)