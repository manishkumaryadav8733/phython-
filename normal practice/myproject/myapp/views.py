from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Create your views here.
class categeoryAPI(APIView):
    def get(self,request):
        return Response("get api calling")

    def post(self,request):
        return Response("post api calling")
def home(request):
    return render(request,"ll.html")
    

