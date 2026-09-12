from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",StudentAPI.as_view())
]