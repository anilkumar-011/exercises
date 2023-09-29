from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class CarSerializer(VehicleSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class TruckSerializer(VehicleSerializer):
    class Meta:
        model = Truck
        fields = '__all__'


class BikeSerializer(VehicleSerializer):
    class Meta:
        model = Bike
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
