from django.urls import *
from ecom.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register("categeories",CategeoryViewSet,basename="categeories")
router.register("product",ProductViewSet,basename="Product")

urlpatterns = [
    path('', include(router.urls))
]