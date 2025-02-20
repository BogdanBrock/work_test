"""Модуль для создания фикстур."""

from uuid import uuid4

import pytest
from django.conf import settings
from django.urls import reverse
from rest_framework.test import APIClient

from wallets.models import Wallet


@pytest.fixture
def api_client():
    """Фикстура для создания API клиента."""
    return APIClient()


@pytest.fixture
def wallet():
    """Фикстура для создания кошелька."""
    return Wallet.objects.create(
        wallet_uuid=str(uuid4()),
        amount=settings.AMOUNT
    )


@pytest.fixture()
def post_wallet_url(wallet):
    """Фикстура для получения адреса."""
    return reverse('post_wallet', args=(wallet.wallet_uuid,))


@pytest.fixture
def form_data():
    """Форма для изменения данных."""
    return {
        'operation_type': settings.WITHDRAW,
        'amount': settings.AMOUNT
    }
