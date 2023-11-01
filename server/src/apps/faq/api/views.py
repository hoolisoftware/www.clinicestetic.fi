from rest_framework import viewsets

from . import serializers
from .. import models


class FAQViewSet(viewsets.ModelViewSet):
    queryset = models.FAQ.objects.all()
    serializer_class = serializers.FAQSerializer
