from django.urls import path, include
from rest_framework import routers
from orm.views import *

router = routers.DefaultRouter()
router.register(r'persons', PersonView, basename='Persons')
# router.register(r'orm1', Orm1.as_view(), basename='Orm scenario -1')

urlpatterns = [
    path('', include(router.urls)),
    path('orm1', Orm1.as_view(), name='Orm scenario -1'),
    path('orm2', Orm2.as_view(), name='Orm scenario -2'),
    path('orm3', Orm3.as_view(), name='Orm scenario -3'),
    path('orm4', Orm4.as_view(), name='Orm scenario -4'),
    path('orm5', Orm5.as_view(), name='Orm scenario -5'),
    path('orm6', Orm6.as_view(), name='Orm scenario -6'),
    path('orm7', Orm7.as_view(), name='Orm scenario -7'),
    path('orm8', Orm8.as_view(), name='Orm scenario -8'),
    path('orm9', Orm9.as_view(), name='Orm scenario -9'),
    path('orm10', Orm10.as_view(), name='Orm scenario -10'),
    path('names', Orm11b.as_view(), name='Orm scenario -11-b'),
    path('names/<int:id>', Orm11c.as_view(), name='Orm scenario -11-c'),
]
