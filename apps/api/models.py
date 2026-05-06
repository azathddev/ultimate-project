from dataclasses import dataclass
import uuid

from django.db import models

from apps.user_auth.models import User


class BlockchainChoices:
    data = {
        "eth": "Ethereum",
        "btc": "Bitcoin",
        "sol": "Solana",
        "ton": "TonCoin",
    }


class Coin(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    short_name = models.CharField(max_length=12)
    blockchain = models.CharField(
        choices=BlockchainChoices.data
    )


class Transaction(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4)
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name="transactions_send")
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name="transactions_receive")
    created_at = models.DateTimeField(auto_now_add=True)
