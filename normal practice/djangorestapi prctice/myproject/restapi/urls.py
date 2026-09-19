from django.urls import path
from restapi.views import *

urlpatterns = [
    path("all",StudentAPI.as_view())
    
]