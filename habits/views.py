from rest_framework import viewsets
from .models import Habit, Notification
from .serializers import HabitSerializer, NotificationSerializer
from .permissions import IsOwnerOrPublicReadOnly
from django.db.models import Q


class HabitViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления привычками.

    Этот ViewSet предоставляет стандартные действия для CRUD операций.
    Права доступа определяются классом IsOwnerOrPublicReadOnly.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrPublicReadOnly]

    def get_queryset(self):
        """
        Возвращает queryset в зависимости от статуса пользователя.

        - Неаутентифицированные пользователи видят только публичные привычки.
        - Администраторы видят все привычки.
        - Аутентифицированные пользователи видят свои привычки и публичные привычки.
        """
        if not self.request.user.is_authenticated:
            # Для неаутентифицированных пользователей возвращаем только публичные привычки
            return Habit.objects.filter(is_public=True)
        if self.request.user.is_staff:
            # Администраторы видят все все привычки
            return Habit.objects.all()
        # Обычные пользователи видят свои привычки + публичные привычки
        return Habit.objects.filter(Q(is_public=True) | Q(user=self.request.user))


class NotificationViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления уведомлениями.

    Этот ViewSet предоставляет стандартные действия для CRUD операций.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        """Возвращаем уведомления только для текущего пользователя."""
        if self.request.user.is_authenticated:
            return Notification.objects.filter(user=self.request.user)
        return Notification.objects.none()  # Пустой queryset для неаутентифицированных пользователей
