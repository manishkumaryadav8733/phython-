from django.shortcuts import render, redirect
from PIL import Image
from myapp.models import *
import os

# Create your views here.
def index(request):
    return render(request,"index.html")


def product(request):
    products=Product.objects.all()
    return render(request,"product.html",{"products":products})


def cart(request):
    return render(request,"cart.html")


def contact(request):
    return render(request,"contact.html")


def productadd(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        image = request.FILES.get("image")

     
    
        Product.objects.create(
            name=name,
            price=price,
            quantity=quantity,
            image=image
             )
    return render(request,"productadd.html")   # After adding product, go back to home page


    



