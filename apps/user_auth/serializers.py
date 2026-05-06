from rest_framework import serializers
from rest_framework.exceptions import ValidationError

import string

from apps.user_auth.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=67)

    def validate(self, attrs):
        if not 6 < len(attrs["username"]) < 20:
            raise ValidationError("username must be at least 6 characters and max 20")

        if not 7 < len(attrs["password"]) < 67:
            raise ValidationError("password must be at least 7 characters and max 67")

        if not set(attrs["password"]).intersection(set(string.digits)):
            raise ValidationError("password must have at least one digit")

        if not set(attrs["password"]).intersection(set(string.ascii_lowercase)):
            raise ValidationError("password must have at least one lowercase letter")

        if not set(attrs["password"]).intersection(set(string.ascii_uppercase)):
            raise ValidationError("password must have at least one uppercase letter")

        if User.objects.filter(username=attrs["username"]).exists():
            raise ValidationError("username exists already")


        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=67)
