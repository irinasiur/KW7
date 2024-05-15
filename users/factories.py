import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    """
    Фабрика для создания объектов модели User для тестирования.

    Атрибуты:
        username (str): Последовательное имя пользователя (user_1, user_2 и т.д.).
        phone_number (str): Последовательный номер телефона (+1234567891, +1234567892 и т.д.).
        password (str): Пароль пользователя, устанавливается с помощью метода set_password.
        is_active (bool): Флаг активности пользователя.
        is_staff (bool): Флаг принадлежности пользователя к административному персоналу.
    """

    class Meta:
        model = User  # Связь с моделью User
        skip_postgeneration_save = True  # Пропуск сохранения после генерации постпоколений

    username = factory.Sequence(lambda n: f"user_{n}")  # Последовательное имя пользователя
    phone_number = factory.Sequence(lambda n: f"+123456789{n}")  # Последовательный номер телефона
    password = factory.PostGenerationMethodCall('set_password', 'testpass')  # Установка пароля
    is_active = True  # Флаг активности по умолчанию
    is_staff = False  # Флаг принадлежности к административному персоналу по умолчанию
