from rest_framework import viewsets

from . import serializers
from .. import models


class PriceViewSet(viewsets.ModelViewSet):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
