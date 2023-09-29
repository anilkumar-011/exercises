from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'cars', CarsView, basename='Cars')
router.register(r'users', UserView, basename='Users')
router.register(r'vehicles', VehiclesView, basename='Vehicles')
router.register(r'trucks', TruckView, basename='Trucks')
router.register(r'bikes', BikeView, basename='Bikes')
router.register(r'shops', ShopView, basename='Shops')
# router.register(r'transaction-api', transaction_api_post, basename='Transaction Api View')

urlpatterns = [
    path('', include(router.urls)),
    path('transaction-api', transaction_api_post, name='Transaction Api View'),
    path('middleware', CustomMiddleware.as_view(), name='Middleware'),
    path('csrfform', csrf_fun, name='CSRF Form'),
    path('csrfform/ajax', csrf_fun_ajax, name='CSRF AJAX form'),
    path('file/html', file_html, name='File form html'),
]
