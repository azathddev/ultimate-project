from django.urls import path

from apps.user_auth.views import login, register, me

urlpatterns = [
    path("login", login),
    path("register", register),
    path("me", me),

]