"""Модуль для создания представлений."""

from adrf.decorators import api_view
from asgiref.sync import sync_to_async
from django.conf import settings
from rest_framework.response import Response

from .serializers import (
    WalletPostSerializer, WalletGetSerializer, validate_data
)


@api_view(('GET',))
async def get_wallet(request, wallet_uuid):
    """Функция для получения счета."""
    wallet = await sync_to_async(validate_data)(wallet_uuid)
    serializer = WalletGetSerializer(wallet)
    return Response(serializer.data)


@api_view(('POST',))
async def post_wallet(request, wallet_uuid):
    """Функция для пополнения и вывода денег со счета."""
    serializer = WalletPostSerializer(
        data=request.data, context={'wallet_uuid': wallet_uuid}
    )
    await sync_to_async(serializer.is_valid)(raise_exception=True)
    wallet = serializer.validated_data.pop('wallet')
    if serializer.validated_data['operation_type'] == settings.DEPOSIT:
        wallet.amount += serializer.validated_data['amount']
    else:
        wallet.amount -= serializer.validated_data['amount']
    await wallet.asave()
    serializer.validated_data['amount'] = wallet.amount
    return Response(serializer.data)
