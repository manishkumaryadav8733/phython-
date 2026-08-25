from django.urls import path
from myapp.views import *


urlpatterns = [

    path("",home,name="home"),
    path("categeory/",categeoryAPI.as_view()),

    
]