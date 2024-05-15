import pytest
from rest_framework import status
from django.urls import reverse
from users.factories import UserFactory
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """
    Фикстура для создания клиента API.

    Возвращает:
        APIClient: Клиент для выполнения запросов к API.
    """
    return APIClient()


@pytest.fixture
def user():
    """
    Фикстура для создания пользователя.

    Возвращает:
        User: Созданный пользователь.
    """
    return UserFactory()


@pytest.mark.django_db
def test_create_habit(api_client, user):
    """
    Тест для проверки создания привычки.

    Аргументы:
        api_client (APIClient): Клиент для выполнения запросов к API.
        user (User): Пользователь, который создает привычку.

    Действия:
        - Аутентификация пользователя.
        - Отправка POST-запроса на создание привычки.
        - Проверка статуса ответа и данных ответа.

    Проверяет:
        - Статус ответа должен быть HTTP 201 Created.
        - Поле 'action' в ответе должно быть 'Read a book'.
    """
    api_client.force_authenticate(user=user)  # Аутентификация пользователя
    url = reverse('habit-list')  # URL для списка привычек
    data = {
        'user': user.id,
        'action': 'Read a book',
        'place': 'Home',
        'time': '18:00:00',
        'is_pleasant': True,
        'frequency': 1,
        'duration': 60
    }
    response = api_client.post(url, data)  # Отправка POST-запроса на создание привычки
    assert response.status_code == status.HTTP_201_CREATED  # Проверка статуса ответа
    assert response.data['action'] == 'Read a book'  # Проверка поля 'action' в ответе
