from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import *
from myapp.serializers import StudentSerializer

class StudentAPI(APIView):

    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students , many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer =StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    def put(self,request,id):
        student = Student.objects.get(id=id)

        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# Create your views here.
