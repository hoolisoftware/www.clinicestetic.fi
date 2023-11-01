from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, 'post')
router.register(r'categories', views.CategoryViewSet, 'category')

urlpatterns = (path('', include(router.urls)),)
