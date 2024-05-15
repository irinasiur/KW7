from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.

    Поля:
        id (int): Идентификатор пользователя.
        username (str): Имя пользователя.
        phone_number (str): Номер телефона пользователя.
        bio (str): Биография пользователя.
        profile_picture (ImageField): Изображение профиля пользователя.
        password (str): Пароль пользователя.
        is_active (bool): Активен ли пользователь.
        is_staff (bool): Является ли пользователь администратором.
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'bio', 'profile_picture', 'password', 'is_active',
                  'is_staff']
        extra_kwargs = {'password': {'write_only': True}}  # Указываем, что пароль не должен возвращаться в ответах

    def create(self, validated_data):
        """
        Создание нового пользователя с использованием метода create_user для корректной обработки пароля.

        Аргументы:
            validated_data (dict): Проверенные данные для создания пользователя.

        Возвращает:
            User: Созданный пользователь.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', None),  # email и другие поля могут быть необязательными
            password=validated_data['password'],
            phone_number=validated_data['phone_number'],
            bio=validated_data.get('bio', ''),  # Пустая строка, если не предоставлено
            profile_picture=validated_data.get('profile_picture', None)  # None, если не предоставлено
        )
        return user
