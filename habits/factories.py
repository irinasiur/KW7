from django.utils import timezone
from users.factories import UserFactory
from .models import Habit
import factory


class HabitFactory(factory.django.DjangoModelFactory):
    """
    Фабрика для создания объектов модели Habit для тестирования.
    Использует библиотеку factory_boy для упрощения создания тестовых данных.
    """

    class Meta:
        model = Habit  # Связь с моделью Habit

    user = factory.SubFactory(UserFactory)  # Создание связанного пользователя с использованием UserFactory
    action = "Drink water"  # Действие по умолчанию
    place = "Office"  # Место по умолчанию
    time = factory.LazyFunction(timezone.now)  # Время выполнения привычки, используется текущее время
    is_pleasant = True  # Признак приятной привычки по умолчанию
    frequency = 1  # Периодичность выполнения привычки в днях
    duration = 60  # Время на выполнение привычки в секундах
    is_public = False  # Признак публичности привычки по умолчанию
