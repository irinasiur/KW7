from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя, расширяющая стандартную модель AbstractUser.

    Атрибуты:
        phone_number (str): Уникальный номер телефона пользователя.
        bio (str): Биография пользователя.
        profile_picture (ImageField): Изображение профиля пользователя.
    """
    phone_number = models.CharField(max_length=15, unique=True, null=False, blank=False)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        """
        Возвращает строковое представление пользователя (username).
        """
        return self.username

    USERNAME_FIELD = 'phone_number'  # Использование номера телефона в качестве основного идентификатора для входа.
    REQUIRED_FIELDS = ['username']  # Указание username как обязательного поля при регистрации.
