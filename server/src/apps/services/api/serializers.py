from rest_framework import serializers

from .. import models


class PriceSerializerBase(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = models.Price
        fields = '__all__'


class PriceSerializer(PriceSerializerBase):
    id = serializers.ReadOnlyField()
    prices = PriceSerializerBase(many=True)

    class Meta:
        model = models.Price
        fields = '__all__'


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    prices = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = models.Service
        fields = '__all__'
