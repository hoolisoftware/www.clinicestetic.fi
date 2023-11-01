from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .. import models
from . import serializers


class ClinicConfigAV(APIView):
    model = models.ClinicConfig
    queryset = models.ClinicConfig.objects.all()
    serializer_class = serializers.ClinicConfigSerializer

    def get(self, request):
        data = self.serializer_class(self.model.load()).data
        return Response(data)


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = models.Certificate.objects.all()
    serializer_class = serializers.CertificateSerializer


class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = models.Specialist.objects.all()
    serializer_class = serializers.SpecialistSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = models.Media.objects.all()
    serializer_class = serializers.MediaSerializer


class BeforeAfterSectionViewSet(viewsets.ModelViewSet):
    queryset = models.BeforeAfterSection.objects.all()
    serializer_class = serializers.BeforeAfterSectionSerializer


class BeforeAfterUnitViewSet(viewsets.ModelViewSet):
    queryset = models.BeforeAfterUnit.objects.all()
    serializer_class = serializers.BeforeAfterUnitSerializer
