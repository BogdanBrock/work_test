"""Модуль для сериализаторов."""

from django.conf import settings
from rest_framework import serializers

from wallets.models import Wallet


def validate_data(wallet_uuid):
    """Функция для валидации данных и получения объекта модели Wallet."""
    wallet = Wallet.objects.filter(
        wallet_uuid=wallet_uuid
    ).first()
    if not wallet:
        raise serializers.ValidationError(
            'Такого счета не существует, введите корректный номер счета .'
        )
    return wallet


class WalletGetSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Wallet."""

    class Meta:
        """Класс Meta для расширения возможностей класса."""

        model = Wallet
        fields = ('amount',)


class WalletPostSerializer(WalletGetSerializer):
    """Сериализатор для модели Wallet."""

    operation_type = serializers.ChoiceField(choices=settings.CHOICES)

    class Meta(WalletGetSerializer.Meta):
        """Класс Meta для расширения возможностей класса."""

        fields = ('operation_type', 'amount')

    def validate(self, data):
        """Метод для валидации данных."""
        wallet = validate_data(self.context['wallet_uuid'])
        if (
            data['amount'] > wallet.amount
            and data['operation_type'] == settings.WITHDRAW
        ):
            raise serializers.ValidationError(
                f'Недостаточно средств. На вашем счете {wallet.amount}'
            )
        data['wallet'] = wallet
        return data
