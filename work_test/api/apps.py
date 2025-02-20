"""Модуль для создания приложения."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Класс ApiConfig создает приложение api."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
