from django.urls import path
from myapp.views import *
from rest_framework import DefaultRouter

urlpatterns = [
    path("",index,name="index")
]