from django.shortcuts import render
from myapp.models import *
from myapp.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def list_student(request):
    return Response("get api calling")

@api_view(["POST"])
def create_student(request):
    return Response("post api calling")

@api_view(["PUT"])
def update_student(request):
    return Response("put api calling")
