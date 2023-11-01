from rest_framework import serializers
from django.contrib.auth import get_user_model

from .. import models


User = get_user_model()


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    categories = CategorySerializer(many=True)
    author = AuthorSerializer()

    class Meta:
        model = models.Post
        fields = '__all__' # noqa
