import time
import base64

from django.core.files.base import ContentFile
from django.template import loader
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.cache import cache
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serialzer import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


# Create your views here.

# ------------redis----------
# stop:  /etc/init.d/redis-server stop
# start:  /etc/init.d/redis-server start

# ------------User------------
class UserView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


# --------------vehicles-------------
class VehiclesView(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def create(self, request, *args, **kwargs):
        cache.clear()
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if cache.get('vehicles'):
            serializer = cache.get('vehicles')
            return Response(serializer)
        else:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            cache.set('vehicles', serializer.data)
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        vehicle_id = kwargs.get('pk')
        if cache.get('vehicles/' + vehicle_id):
            serializer = cache.get('vehicles/' + vehicle_id)
            return Response(serializer)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            cache.set('vehicles/' + vehicle_id, serializer.data, timeout=60)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        cache.clear()
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        cache.clear()
        return super().destroy(request, *args, **kwargs)


# ------------Cars----------------
class CarsView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        cache.clear()
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if cache.get('cars'):
            data = cache.get('cars')
            return Response(data)
        else:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            cache.set('cars', serializer.data)
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        car_id = kwargs.get('pk')
        if cache.get('cars/' + car_id):
            return Response(cache.get('cars/' + car_id))
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            cache.set('cars/' + car_id, serializer.data)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        cache.clear()
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        cache.clear()
        return super().destroy(request, *args, **kwargs)


# ----------------Trucks---------------
class TruckView(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

    def create(self, request, *args, **kwargs):
        cache.clear()
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if cache.get('trucks'):
            data = cache.get('trucks')
            return Response(data)
        else:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            cache.set('trucks', serializer.data)
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        truck_id = kwargs.get('pk')
        if cache.get('trucks/' + truck_id):
            return Response(cache.get('trucks/' + truck_id))
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            cache.set('trucks/' + truck_id, serializer.data)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        cache.clear()
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        cache.clear()
        return super().destroy(request, *args, **kwargs)


# --------------Bike--------------
class BikeView(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

    def create(self, request, *args, **kwargs):
        cache.clear()
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if cache.get('bikes'):
            data = cache.get('bikes')
            return Response(data)
        else:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            cache.set('bikes', serializer.data)
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        bike_id = kwargs.get('pk')
        if cache.get('bikes/' + bike_id):
            return Response(cache.get('bikes/' + bike_id))
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            cache.set('bikes/' + bike_id, serializer.data)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        cache.clear()
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        cache.clear()
        return super().destroy(request, *args, **kwargs)


# ------------Shop----------------
class ShopView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def create(self, request, *args, **kwargs):
        cache.clear()
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if cache.get('shops'):
            data = cache.get('shops')
            return Response(data)
        else:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            cache.set('shops', serializer.data)
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        shop_id = kwargs.get('pk')
        if cache.get('shops/' + shop_id):
            return Response(cache.get('shops/' + shop_id))
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            cache.set('shops/' + shop_id, serializer.data)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        cache.clear()
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        cache.clear()
        return super().destroy(request, *args, **kwargs)


# -----------------Transaction API------------------------

@transaction.atomic
@api_view(['POST', 'GET'])
def transaction_api_post(request):
    if request.method == 'GET':
        query_id = request.GET.get('id', None)
        if not query_id:
            return JsonResponse({'error': 'Missing transaction ID.'}, status=400)
        data = Vehicle.objects.get(pk=query_id)
        if not data:
            return JsonResponse({'error': 'Objects does`t exists.'}, status=400)
        time.sleep(10)
        data.lp_number = 5001
        data.save()
        return JsonResponse({'data': 'Object exists'})

    if request.method == 'POST':
        data = request.data

        vehicle = data.get('vehicle', None)
        vehicle = Vehicle(lp_number=vehicle.get('lp_number', None),
                          wheel_count=vehicle.get('wheel_count', None),
                          manufacture=vehicle.get('manufacture', None),
                          model_name=vehicle.get('model_name', None),
                          file=vehicle.get('file', None),
                          )
        vehicle.save()

        # serializer = VehicleSerializer(data=data.get('vehicle', None))
        # if serializer.is_valid():
        #     serializer.save()
        # else:
        #     raise serializers.ValidationError()

        bike = data.get('bike', None)
        bike = Bike(lp_number=bike.get('lp_number', None),
                    wheel_count=bike.get('wheel_count', None),
                    manufacture=bike.get('manufacture', None),
                    model_name=bike.get('model_name', None),
                    milage=bike.get('milage', None),
                    file=bike.get('file', None),
                    )
        bike.save()

        # serializer = BikeSerializer(data=data.get('bike', None))
        # if serializer.is_valid():
        #     serializer.save()
        # else:
        #     raise serializers.ValidationError()

        truck = data.get('truck', None)
        truck = Truck(lp_number=truck.get('lp_number', None),
                      wheel_count=truck.get('wheel_count', None),
                      manufacture=truck.get('manufacture', None),
                      model_name=truck.get('model_name', None),
                      file=truck.get('file', None),
                      max_goods_weight=truck.get('max_goods_weight', None)
                      )
        truck.save()

        # serializer = TruckSerializer(data=data.get('truck', None))
        # if serializer.is_valid():
        #     serializer.save()
        # else:
        #     raise serializers.ValidationError()

        shop = data.get('shop', None)
        shop = Shop(name=shop.get('name', None))
        shop.save()

        # serializer = ShopSerializer(data=data.get('shop', None))
        # if serializer.is_valid():
        #     serializer.save()
        # else:
        #     raise serializers.ValidationError()

        car = data.get('car', None)
        car = Car(lp_number=car.get('lp_number', None),
                  wheel_count=car.get('wheel_count', None),
                  manufacture=car.get('manufacture', None),
                  model_name=car.get('model_name', None),
                  is_air_conditioned=car.get('is_air_conditioned', None),
                  has_roof_top=car.get('has_roof_top', None),
                  file=car.get('file', None),
                  )
        car.save()

        # serializer = CarSerializer(data=data.get('car', None))
        # if serializer.is_valid():
        #     serializer.save()
        # else:
        #     raise serializers.ValidationError()

        return HttpResponse('Posted Successfully')


# ---------------middleware---------------
class CustomMiddleware(APIView):
    def get(self, request):
        data = request.data
        return Response(data, 200)


# ------------csrf------------------
@api_view(['GET', 'POST'])
def csrf_fun(request):
    if request.method == 'GET':
        html = loader.get_template('csrf.html')
        return HttpResponse(html.render({}, request))
    if request.method == 'POST':
        data = request.data
        return Response(data, 200)


@api_view(['GET', 'POST'])
def csrf_fun_ajax(request):
    if request.method == 'GET':
        html = loader.get_template('csrf_ajax.html')
        return HttpResponse(html.render({}, request))
    if request.method == "POST":
        data = request.data
        print(data)
        return Response(data.values(), 200)


# -------------------file upload--------------

@api_view(['GET', 'POST'])
def file_html(request):
    if request.method == 'GET':
        html = loader.get_template('file upload.html')
        return HttpResponse(html.render({}, request))
    if request.method == 'POST':
        data = request.data
        name = data.get('name')
        uploaded_file = request.FILES['document']
        file_content = uploaded_file.read()

        # Encode the content as base64
        encoded_content = base64.b64encode(file_content).decode('utf-8')

        student = Student(name=name)
        student.file.save(str(name) + '.pdf', ContentFile(file_content))
        student.save()
        return Response({'message': 'File uploaded successfully.'}, 200)
