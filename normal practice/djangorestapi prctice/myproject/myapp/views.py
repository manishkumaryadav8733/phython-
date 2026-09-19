from django.shortcuts import render
from rest_framework.response import Response 
from myapp.serializers import *
from rest_framework.decorators import api_view
from myapp.models import *
from rest_framework import status

@api_view(['POST'])
def create_api(request):
    return Response("post api caliing")

@api_view(['GET'])
def list_api(request):
    return Response("get api calling")

@api_view(['PUT'])
def update_api(request):
    return Response("put api calling" )

@api_view(["DELETE"])
def delete_api(request):
    return Response("delete api calling")

# Create your views here.
@api_view(["POST"])
def create_student(request):
    data = request.data
    ser = StudentSerializers(data=data)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"something went Wrong"},status=status.HTTP_400_BAD_REQUEST)
    else:
        ser.save()
        return Response({"data":ser.data,"message":"student created"},status=status.HTTP_201_CREATED)

@api_view(["GET"])
def list_student(request):
    stu = Student.objects.all()
    ser = StudentSerializers(stu,many=True)
    return Response({"data":ser.data},status=status.HTTP_200_OK)

@api_view(["GET"])
def retrive_student(request,id):
    try :
        stud = Student.objects.get(id=id)
        ser = StudentSerializers(stud,many=True)
        return Response({"data":ser.data},status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response({"data":"something went wrong"},status=status.HTTP_200_OK)

@api_view(["PUT"])
def update_student(request,id):
    try :
        stu = Student.objects.get(id=id)
        ser = StudentSerializers(stu,request.data,partial=True)
        if not ser.is_valid():
            return Response({"errors":ser.data,"message":"something went wrong "},status=status.HTTP_400_BAD_REQUEST)
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Stdent updated"},status=status.HTTP_201_CREATED)
    except Student.DoesNotExist:
        return Response({"message":"Student not found"},status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_student(request,id):

    try :
        student = Student.objects.get(id=id)
        student.delete()
        return Response({"data":"Student deleted"},status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response({"data":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)













        

