"""Модуль для создания данных в БД."""

from uuid import uuid4

from django.core.management import BaseCommand

from wallets.models import Wallet


class Command(BaseCommand):
    """Менеджмент-скрипт для создания данных в БД."""

    def handle(self, *args, **options):
        """Функция для сохранения данных в БД."""
        Wallet.objects.bulk_create(
            Wallet(wallet_uuid=str(uuid4())) for _ in range(4)
        )
        self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))
