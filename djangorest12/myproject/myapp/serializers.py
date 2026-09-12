from rest_framework import serializers
from myapp.models import *

class EmployeSerializer(serializers.ModelSerializer):
    class meta:
        model = Employe
        fields = '__all__'