from django.shortcuts import render
from rest_framework.response import Response
from myapp.models import *
from myapp.serializers import *
from rest_framework.decorators import api_view,APIView
from rest_framework import status

# Create your views here.

class Employeapi(APIView):
    def get(self,request,id):
        emp = Employe.objects.get(id=id)
        ser = EmployeSerializer(emp)
        if not ser.is_valid():
            return Response({"data":ser.data})
        return Response({"message":"employe not found"})
    def post(self,request,id):
        emp = Employe.objects.get(id=id)
        ser = EmployeSerializer(emp,request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"somethingt went wromg"},status=status.HTTPS_400_BAD_REQUEST)
        else:
            ser.save()
            return Response({"data":ser.data

            })