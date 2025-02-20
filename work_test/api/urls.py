"""Модуль для создания маршрутов."""

from django.urls import path

from .views import get_wallet, post_wallet

urlpatterns = [
    path(
        'wallets/<wallet_uuid>/',
        get_wallet,
        name='get_wallet'
    ),
    path(
        'wallets/<wallet_uuid>/operation/',
        post_wallet,
        name='post_wallet'
    )
]
