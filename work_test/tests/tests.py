"""Модуль для тестирования основного кода."""

import pytest
from django.conf import settings
from django.urls import reverse
from rest_framework import status


pytestmark = pytest.mark.django_db


class TestEndPoints:
    """Тесты для проверки работы эндпоинтов."""

    def test_get_balance(self, api_client, wallet):
        """Проверка получения счета."""
        url = reverse('get_wallet', args=(wallet.wallet_uuid,))
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_deposit_balance(
        self, api_client, wallet, post_wallet_url, form_data
    ):
        """Проверка добавления денег на счет."""
        form_data['operation_type'] = settings.DEPOSIT
        expected_result = wallet.amount + settings.AMOUNT
        response = api_client.post(post_wallet_url, data=form_data)
        wallet.refresh_from_db()
        assert wallet.amount == expected_result
        assert response.status_code == status.HTTP_200_OK

    def test_withdraw_balance(
        self, api_client, wallet, post_wallet_url, form_data
    ):
        """Проверка списания денег со счета."""
        expected_result = wallet.amount - settings.AMOUNT
        response = api_client.post(post_wallet_url, data=form_data)
        wallet.refresh_from_db()
        assert wallet.amount == expected_result
        assert response.status_code == status.HTTP_200_OK


class TestContent:
    """Тесты для проверки наличия контента."""

    def test_wrong_data_for_get_balance(self, api_client, wallet):
        """Неправильные данные для показа счета."""
        url = reverse('get_wallet', args=(wallet.wallet_uuid,))
        response = api_client.get(url)
        data = response.json()
        assert 'amount' in data, (
            'Отсутствует поле "amount" для показа баланса.'
        )
        assert len(data) <= 1, 'Больше одного поля для вывода данных.'

    def test_wrong_data_for_change_balance(
        self, api_client, post_wallet_url, form_data
    ):
        """Неправильные данные для изменения счета."""
        response = api_client.post(post_wallet_url, data=form_data)
        data = response.json()
        assert 'operation_type' in data, (
            'Запрос должен содержать поле "operation_data".'
        )
        assert 'amount' in data, 'Запрос должен содержать поле "amount".'
        assert len(data) <= 2, 'Запрос содержит в себе больше 2 полей.'


class TestLogic:
    """Тесты для проверки логики."""

    def test_balance_cant_has_negative_number(
        self, api_client, wallet, post_wallet_url, form_data
    ):
        """Счет не может быть отрицательным."""
        form_data['amount'] = 501
        response = api_client.post(post_wallet_url, data=form_data)
        wallet.refresh_from_db()
        assert wallet.amount >= 0, 'Счет не может быть отрицательным'
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.parametrize(
        'number', (-1, 0)
    )
    def test_amount_cant_has_negative_or_zero_number(
        self, api_client, post_wallet_url, form_data, number
    ):
        """
        Запрос на снятие денег с счета не может быть отрицательным числом.

        Так же запрос не может иметь нулевое значение.
        """
        form_data['amount'] = number
        response = api_client.post(post_wallet_url, data=form_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST, (
            'Снять или положить деньги со счета можно начиная с 1.'
        )
