import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """
    Фикстура для создания клиента API.

    Возвращает:
        APIClient: Клиент для выполнения запросов к API.
    """
    return APIClient()


@pytest.mark.django_db
def test_register_user(api_client):
    """
    Тест для проверки регистрации нового пользователя.

    Аргументы:
        api_client (APIClient): Клиент для выполнения запросов к API.

    Действия:
        - Отправка POST-запроса на регистрацию нового пользователя.
        - Проверка статуса ответа и данных ответа.

    Проверяет:
        - Статус ответа должен быть HTTP 201 Created.
        - Поле 'username' в ответе должно быть 'newuser'.
    """
    url = reverse('user-register')  # URL для регистрации пользователя
    data = {
        'username': 'newuser',
        'phone_number': '+1234567890',
        'password': 'testpassword123'
    }
    response = api_client.post(url, data)  # Отправка POST-запроса на регистрацию
    print(response.data)  # Вывод данных ответа
    assert response.status_code == status.HTTP_201_CREATED  # Проверка статуса ответа
    assert response.data['username'] == 'newuser'  # Проверка поля 'username' в ответе
