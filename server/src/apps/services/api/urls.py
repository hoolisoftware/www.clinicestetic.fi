from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'prices', views.PriceViewSet, 'price')
router.register(r'services', views.ServiceViewSet, 'service')

urlpatterns = (path('', include(router.urls)),)
