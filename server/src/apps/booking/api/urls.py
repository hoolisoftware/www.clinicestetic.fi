from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('form-feedback', views.FormFeedbackViewSet)
router.register('form-phone', views.FormPhoneViewSet)
router.register('booking', views.BookingViewSet)
router.register('booking-sessions', views.BookingSessionViewSet)

urlpatterns = (
    path('', include(router.urls)),
)
