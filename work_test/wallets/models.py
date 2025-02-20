"""Модуль для создания моделей."""

from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Wallet(models.Model):
    """Класс для создания модели Wallet."""

    wallet_uuid = models.CharField(
        'Счет клиента', max_length=settings.MAX_LENGTH, unique=True
    )
    amount = models.DecimalField(
        'Баланс счета',
        max_digits=50,
        decimal_places=2,
        default=0,
        validators=(
            MinValueValidator(Decimal('1')),
        )
    )

    class Meta:
        """Класс Meta для расширения возможностей класса."""

        verbose_name = 'кошелек'
        verbose_name_plural = 'Кошельки'

    def __str__(self):
        """Магический метод, который определяет название объекта."""
        return f'Номер счета {self.wallet_uuid}'
