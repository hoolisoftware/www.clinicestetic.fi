from drf_recaptcha.fields import ReCaptchaV2Field
from rest_framework import serializers

from .. import models


class RecaptchaMixin():

    recaptcha = ReCaptchaV2Field()

    def validate(self, attrs):
        attrs.pop("recaptcha")
        return attrs


class FormFeedbackSerializer(serializers.ModelSerializer, RecaptchaMixin):
    class Meta:
        model = models.FormFeedback
        fields = '__all__'


class FormPhoneSerializer(serializers.ModelSerializer, RecaptchaMixin):

    class Meta:
        model = models.FormPhone
        fields = '__all__'


class BookingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookingSession
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer, RecaptchaMixin):
    class Meta:
        model = models.Booking
        fields = '__all__'

    session = serializers.PrimaryKeyRelatedField(queryset=models.BookingSession.objects.all()) # noqa
