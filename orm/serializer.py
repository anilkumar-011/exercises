from rest_framework import serializers
from .models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class NameSerializer(serializers.Serializer):
    class Meta:
        model = Name
        fields = '__all__'
