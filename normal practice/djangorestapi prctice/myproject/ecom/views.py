from django.shortcuts import render
from ecom.models import *
from ecom.serializers import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
 

# Create your views here.
class CategeoryViewSet(viewsets.ModelViewSet):
    queryset = Categeory.objects.all()
    serializer_class = CategeorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


