from rest_framework import serializers

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name')


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name')


class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
