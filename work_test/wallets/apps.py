"""Модуль для создания приложения."""

from django.apps import AppConfig


class WalletsConfig(AppConfig):
    """Класс WalletsConfig создает приложение wallets."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wallets'
    verbose_name = 'Каталог кошельков'
