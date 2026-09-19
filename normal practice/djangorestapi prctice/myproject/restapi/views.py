from django.shortcuts import render
from restapi.models import *
from restapi.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework import status


 
# Create your views here.
class StudentAPI(APIView):
    def get(self,request):
        try :
            stu = Student.objects.all()
            ser = StudentSerializer(stu,many=True)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"message":"student not found"})

    def post(self,request):
        try:
            ser = StudentSerializer(data=request.data)
            if not ser.is_valid():
                return Response({"errors":ser.errors,"message":"something went wrong"})
            else:
                ser.save()
                return Response({"data":ser.data,"message":"student created"},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":e})
    def put(self,request):
        try:
            stu = Student.objects.get(id=id)
            ser = StudentSerializer(data=request.data)
            if not ser.is_valid:
                return Response({"data":ser.data,"message":"Student update"},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":e})

        def delete(self,request,id):
            try:
                stu = Student.objects.get(id=id)
                stu.delete()
                return Response({"message":"emp deleted"})
            except Student.DoesNotExist as e:
                return Response({"message":"Sutdent not found"})