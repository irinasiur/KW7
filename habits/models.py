from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Habit(models.Model):
    """
    Модель для представления привычек пользователей.

    Атрибуты:
        user (ForeignKey): Ссылка на модель пользователя.
        action (CharField): Описание действия привычки.
        place (CharField): Место выполнения привычки.
        time (TimeField): Время выполнения привычки.
        is_pleasant (BooleanField): Признак приятной привычки.
        linked_habit (ForeignKey): Связанная привычка.
        frequency (IntegerField): Периодичность выполнения привычки в днях.
        reward (CharField): Вознаграждение за выполнение привычки.
        duration (IntegerField): Время на выполнение привычки в секундах.
        is_public (BooleanField): Признак публичной привычки.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="habits")

    # Основные текстовые поля для описания привычки
    action = models.CharField(max_length=200, verbose_name="Действие")
    place = models.CharField(max_length=100, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")

    # Булево поле для определения, является ли привычка приятной
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")

    # Опциональная связь привычки с другой привычкой
    linked_habit = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Связанная привычка", limit_choices_to={'is_pleasant': True}
    )

    # Периодичность выполнения привычки в днях
    frequency = models.IntegerField(
        default=1, verbose_name="Периодичность (дни)",
        validators=[MinValueValidator(1), MaxValueValidator(7)]
    )

    # Опциональное вознаграждение за выполнение привычки
    reward = models.CharField(max_length=200, null=True, blank=True, verbose_name="Вознаграждение")

    # Ограничение времени на выполнение привычки в секундах
    duration = models.IntegerField(
        default=120, verbose_name="Время на выполнение (секунды)",
        validators=[MaxValueValidator(120)]
    )

    # Булево поле для определения, может ли привычка быть публичной
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")

    def __str__(self):
        """
        Возвращает строковое представление объекта Habit.
        """
        return f"{self.user.username}: {self.action} at {self.time} in {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def clean(self):
        """
        Переопределение метода clean для валидации полей модели.
        """
        if self.linked_habit and self.reward:
            raise ValidationError("Не может быть одновременно выбрано вознаграждение и связанная привычка.")
        if self.duration > 120:
            raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


class Notification(models.Model):
    """
    Модель для представления уведомлений о привычках пользователей.

    Атрибуты:
        user (ForeignKey): Ссылка на модель пользователя.
        habit (ForeignKey): Ссылка на модель привычки.
        message (TextField): Сообщение уведомления.
        send_time (DateTimeField): Время отправки уведомления.
        sent (BooleanField): Статус отправки уведомления.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField(verbose_name="Сообщение уведомления")
    send_time = models.DateTimeField(verbose_name="Время отправки")
    sent = models.BooleanField(default=False, verbose_name="Статус отправки")

    def __str__(self):
        """
        Возвращает строковое представление объекта Notification.
        """
        return f"Уведомление для {self.user.username} о привычке '{self.habit.action}' на" \
               f" {self.send_time.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"
