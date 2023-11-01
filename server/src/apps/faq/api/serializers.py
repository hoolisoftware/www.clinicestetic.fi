from rest_framework import serializers

from .. import models


class FAQSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FAQ
        fields = '__all__'
