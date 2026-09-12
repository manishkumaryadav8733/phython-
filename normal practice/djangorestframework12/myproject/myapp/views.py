from django.shortcuts import render
from rest_framework.decorators import APIViews,api_view
from myapp.models import *
from myapp.serializer import *
from rest_framework import status


# Create your views here.
class StudentApi(APIViews):
    def post(self,request):
        try:
            ser = StudentSerializer(data)
