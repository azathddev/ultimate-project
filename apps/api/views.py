from rest_framework.views import APIView
from rest_framework import status

from apps.api.models import Transaction, Coin
from apps.api.serializers import TransactionSerializer, CoinSerializer
from apps.common.utils import response
from apps.common.permissions import IsAuthed

from rest_framework.response import Response


class HealthCheck(APIView):
    def get(self, request):
        return Response({"detail": "ok"})


class TransactionAPIView(APIView):
    permission_classes = [IsAuthed]
    serializer = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.all()

    def get(self, request):
        return self.serializer(self.get_queryset(), many=True)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if not serializer.is_valid():
            return response(
                "Validation Error",
                {"detail": serializer.errors},
                status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        serializer.save()
        return response(
            "Transaction created successful",
            serializer.validated_data,
            status.HTTP_201_CREATED,
        )


class CoinAPIView(APIView):
    permission_classes = [IsAuthed]
    serializer = CoinSerializer

    def get_queryset(self):
        return Coin.objects.all()

    def get(self, request):
        return Response(self.serializer(self.get_queryset(), many=True).data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if not serializer.is_valid():
            return response(
                "Validation Error",
                {"detail": serializer.errors},
                status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        serializer.save()
        return response(
            "Coin created successful",
            serializer.validated_data,
            status.HTTP_201_CREATED,
        )
