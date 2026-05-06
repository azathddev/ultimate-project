from django.contrib import admin

from apps.api.models import Coin, Transaction

admin.site.register(Coin)
admin.site.register(Transaction)
