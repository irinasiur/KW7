from .models import Habit, Notification
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habit.

    Поля:
        user (PrimaryKeyRelatedField): Идентификатор пользователя, связанного с привычкой.
        id (int): Идентификатор привычки.
        action (str): Действие, описывающее привычку.
        place (str): Место выполнения привычки.
        time (time): Время выполнения привычки.
        is_pleasant (bool): Признак приятной привычки.
        linked_habit (int): Идентификатор связанной привычки.
        frequency (int): Периодичность выполнения привычки в днях.
        reward (str): Вознаграждение за выполнение привычки.
        duration (int): Время на выполнение привычки в секундах.
        is_public (bool): Признак публичной привычки.
        user_id (int): Идентификатор пользователя.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Habit
        fields = [
            'id', 'user', 'action', 'place', 'time',
            'is_pleasant', 'linked_habit', 'frequency', 'reward',
            'duration', 'is_public', 'user_id'
        ]


class NotificationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Notification.

    Поля:
        user (str): Имя пользователя, связанного с уведомлением.
        habit (str): Действие, описывающее привычку.
        id (int): Идентификатор уведомления.
        message (str): Сообщение уведомления.
        send_time (datetime): Время отправки уведомления.
        sent (bool): Статус отправки уведомления.
    """
    user = serializers.ReadOnlyField(source='user.username')
    habit = serializers.ReadOnlyField(source='habit.action')

    class Meta:
        model = Notification
        fields = ['id', 'user', 'habit', 'message', 'send_time', 'sent']
