from django.conf.urls import url
from django.urls import include,path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^home/', views.LandingPage.as_view()),
]