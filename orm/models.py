from django.db import models
from app.models import Vehicle


# Create your models here.
class Person(models.Model):
    ID = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)

    # one_to_many=models.

    def __str__(self):
        return str(self.name) + ' id:' + str(self.ID)


class Name(models.Model):
    text = models.CharField(max_length=20, db_index=True)

    def __str__(self): return str(self.text)



class A(models.Model):
    a = models.CharField(max_length=20)

    def str(self): return str(self.a)


class B(models.Model):
    b = models.CharField(max_length=20)

    def str(self): return str(self.b)


class C(models.Model):
    c = models.CharField(max_length=20)

    def str(self): return str(self.c)


class X(models.Model):
    x = models.CharField(max_length=20)
    a = models.ForeignKey(A, on_delete=models.CASCADE)
    b = models.ManyToManyField(B)
    c = models.OneToOneField(C, on_delete=models.CASCADE, null=True)

    def str(self): return str(self.x)

    def b_values(self):
        b = []
        for i in self.b.all(): b.append(i)
        return b


class D(models.Model):
    d = models.CharField(max_length=20)
    x = models.ForeignKey(X, on_delete=models.CASCADE, null=True)  # one-to-many relation for X class

    def str(self): return str(self.d)

