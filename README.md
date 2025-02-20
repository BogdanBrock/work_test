## 💻 Технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![Gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)

## Описание тестового задания.

- Это тестовое задание в котором мы можем получать данные со счета, 
а так же класть или снимать деньги со счета. В тестовом задании 
реализован DRF, где мы можем десериализовать и сериализовать такие 
методы как: POST и GET, но так же валидировать данные. 
В тестовом задании присутствуют тесты, которые сводят 
дальнейшие ошибки к минимуму, присутствует докер-контейнеризация 
для дальнейше работы с проектом на различных компьютерах.

## Инструкция как развернуть проект в докере

- Нужно склонировать проект из репозитория командой:
```bash
git clone git@github.com:BogdanBrock/work_test.git
```
- Для дальнейшей работы с докером нужно создать файл ".env".
Пример для его создания есть в корне, файл называется ".env.example".

- Находясь в корневой папке проекта выполните команду:
```bash
docker compose up
```

- После того как докер-контейнеры будут активированы, 
открываем другое окно и для лучшего отображения админ-зоны, 
мы можем собрать статику командой:
```bash
docker compose exec backend python manage.py collectstatic
```

- После сбора, мы должны передать ее в контейнер nginx,
после чего статика будет раздаваться, команда для
перемещения статики:
```bash
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```

- Применение миграций командой:
```bash
docker compose exec backend python manage.py makemigrations
```

- Для создания базы данных мы
используем следующую команду:
```bash
docker compose exec backend python manage.py migrate
```

- Так же по желанию можно создать супер пользователя
для того, чтобы управлять админ-зоной:
```bash
docker compose exec backend python manage.py createsuperuser
```

- Помимо всех базовых команд, есть management-команда
для заполнения базы данных:
```bash
docker compose exec backend python manage.py load_data 
```

- Выполнив все необходимые команды,
мы можем использовать эндпоинты ниже.

- Для примера можем использовать этот эндпоинт:
```bash
127.0.0.1/8000/api/v1/wallets/<wallet_uuid>/operation/
```
- Для пополнения счета используем такой json формат:
```json
{
  "operation_type": "deposit",
  "amount": 50
}
```
- Для снятия денег со счета используем такой формат:
```json
{
  "operation_type": "withdraw",
  "amount": 50
}
```

## Список адресов доступных после создания контейнеров
--------------------------------------------------------------------------------------------------------
|                           Адрес                             |              Описание                  |
|:------------------------------------------------------------|:---------------------------------------|
| 127.0.0.1:8000/admin/                                       | Для входа в админ-зону                 |
| 127.0.0.1:8000/api/v1/wallets/<wallet_uuid>/                | Для получения счета                    |
| 127.0.0.1/8000/api/v1/wallets/<wallet_uuid>/operation/      | Для пополнения и снятия денег со счета |
--------------------------------------------------------------------------------------------------------
