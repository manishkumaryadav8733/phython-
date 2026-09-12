from django.shortcuts import render
from myapp.models import *
from myapp.forms import *


# Create your views here.
def index(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        form.save()
        return render(request,"index.html",{"form":form})
    
    return render(request,"index.html",{"form":form})
