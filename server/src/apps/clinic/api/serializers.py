from rest_framework import serializers

from .. import models


class ClinicConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClinicConfig
        fields = '__all__'


class CertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Certificate
        fields = '__all__'


class SpecialistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Specialist
        fields = '__all__'


class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Media
        fields = '__all__'


class BeforeAfterUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BeforeAfterUnit
        fields = '__all__'


class BeforeAfterSectionSerializer(serializers.ModelSerializer):
    units = BeforeAfterUnitSerializer(many=True)

    class Meta:
        model = models.BeforeAfterSection
        fields = '__all__'
