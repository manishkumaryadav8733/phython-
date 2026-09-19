from rest_framework.serializers import ModelSerializer
from ecom.models import *

class CategeorySerializer(ModelSerializer):
    class Meta:
        model = Categeory
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
            model = Product
            fields = '__all__'

    def to_representation(self,instance):
        resp = super().to_representation(instance)
        resp['categeory']=CategeorySerializer(instance.categeory).data
        return resp
