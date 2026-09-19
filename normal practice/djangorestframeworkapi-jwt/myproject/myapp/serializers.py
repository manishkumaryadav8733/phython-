from rest_framework.serializers import ModelSerializer
from myapp.models import *

class EmployeSerializers(ModelSerializer):
    class Meta:
        models = Employe
        fields = '__all__'

