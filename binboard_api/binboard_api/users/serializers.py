from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.CharField()
    real_name = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'real_name',
            'password'
        ]


class PublicUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        fields = [
            'username'
        ]
