from rest_framework import serializers
from myapp.models import *

class StudentSerializer(serializers.Modelserializer):
    class Meta:
        model = "Student"
        fields = '__all__'
