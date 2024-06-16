#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'