from django.urls import path

from apps.api.views import CoinAPIView, TransactionAPIView, HealthCheck

urlpatterns = [
    path("coins", CoinAPIView.as_view()),
    path("transactions", TransactionAPIView.as_view()),
    path("health", HealthCheck.as_view()),
]
