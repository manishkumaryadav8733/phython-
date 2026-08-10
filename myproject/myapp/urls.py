from django.urls import *
from myapp.views import *


urlpatterns =[
    path("",index,name="index"),
    path("product",product,name="product"),
    path("cart",cart,name="cart"),
    path("contact",contact,name="contact"),
    path("productadd",productadd,name="productadd"),
    
    
]
