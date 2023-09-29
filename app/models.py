from django.contrib.auth.models import User
from django.db import models


# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver

# Create your models here.
# Vehicle fields are: lp_number, wheel_count, manufacturer, model_name
# Car  fields are: lp_number, wheel_count, manufacturer, model_name, is_air_conditioned, has_roof_top
# Truck  fields are: lp_number, wheel_count, manufacturer, model_name, max_goods_weight
# Final Expectation:
# Car.objects.all() should return all cars
# Truck.objects.all() should return all trucks
# Vehicle.objects.all() should return all cars + trucks + vehicles


class Vehicle(models.Model):
    lp_number = models.IntegerField()
    wheel_count = models.IntegerField()
    manufacture = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)

    # owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # file = models.FileField(default=None, null=True)

    def __str__(self): return self.manufacture + ' ' + self.model_name

    class Meta:
        ordering = ['manufacture']


class Car(Vehicle):
    is_air_conditioned = models.BooleanField(null=False)
    has_roof_top = models.BooleanField(null=False)

    def __str__(self): return self.manufacture + ' ' + self.model_name


class Truck(Vehicle):
    max_goods_weight = models.IntegerField(null=False)

    # super.owner = models.OneToOneRel(User, on_delete=models.PROTECT())

    def __str__(self): return self.manufacture + ' ' + self.model_name


class Shop(models.Model):
    name = models.CharField(max_length=100)

    # owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self): return str(self.name)


class Bike(Vehicle):
    milage = models.IntegerField(null=False)

    def __str__(self): return str(self.manufacture) + str(self.model_name)


class Student(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField()

    def __str__(self):return str(self.name)