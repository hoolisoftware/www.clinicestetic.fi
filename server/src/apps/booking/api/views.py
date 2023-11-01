from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .. import models
from . import serializers


class FormFeedbackViewSet(viewsets.ModelViewSet):
    queryset = models.FormFeedback.objects.all()
    serializer_class = serializers.FormFeedbackSerializer
    permission_classes = []


class FormPhoneViewSet(viewsets.ModelViewSet):
    queryset = models.FormPhone.objects.all()
    serializer_class = serializers.FormPhoneSerializer
    permission_classes = []


class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']


class BookingSessionViewSet(viewsets.ModelViewSet):
    queryset = models.BookingSession.objects.all()
    serializer_class = serializers.BookingSessionSerializer
    permission_classes = []
