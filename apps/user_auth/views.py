from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from apps.user_auth.serializers import RegisterSerializer, LoginSerializer
from apps.common.utils import response


@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if not serializer.is_valid():
        return response(
            "Validation Error",
            serializer.errors,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    user = serializer.save()

    token, created = Token.objects.get_or_create(user=user)
    return response(
        "Successful register",
        {
            "username": user.username,
            "token": token.key
        },
        status.HTTP_201_CREATED
    )


@api_view(["POST"])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(
            {
                "message": "Validation Error",
                "detail": serializer.errors
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    user = authenticate(**serializer.validated_data)

    if not user:
        return Response(
            {
                "message": "Authenticate Error",
                "detail": "Invalid credentials"
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    token, created = Token.objects.get_or_create(user=user)

    return response(
        "Successful log in",
        {
            "username": user.username,
            "token": token.key
        },
        status.HTTP_200_OK
    )


@api_view(["GET"])
def me(request):
    if not hasattr(request.user, "username"):
        return response(
            "Authenticate Error",
            {
                "detail": "Credentials is not provided"
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    return response("Successful log in",
                    {
                        "username": request.user.username
                    },
                    status.HTTP_200_OK
                    )
