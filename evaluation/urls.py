from django.conf.urls import url
from django.urls import include,path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^test-inicial/', views.TestInitial.as_view()),
    url(r'^send-evaluation/$',views.SendEvaluationAPI.as_view()),
    url(r'^registration-school/', views.RegistrationSchool.as_view()),
]