from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer
from habits.permissions import IsSelfOrAdmin
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления пользователями.

    Этот ViewSet предоставляет стандартные действия для CRUD операций.
    Права доступа устанавливаются в зависимости от типа запроса.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Переопределение метода для установки разрешений в зависимости от типа запроса.

        - Для создания пользователя (регистрация) разрешаем доступ всем.
        - Для остальных действий требуется аутентификация и проверка прав доступа.
        """
        if self.action == 'create':
            # Разрешаем неаутентифицированным пользователям регистрацию
            permission_classes = [permissions.AllowAny]
        else:
            # Для всех других действий требуется аутентификация и проверка является ли пользователь владельцем профиля или администратором
            permission_classes = [IsAuthenticated, IsSelfOrAdmin]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """
        Возвращает queryset пользователей в зависимости от прав пользователя.

        - Администраторы видят всех пользователей.
        - Обычные пользователи видят только свой профиль.
        """
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        """
        Возвращает объект пользователя, проверяя права доступа.

        - Администраторы могут получить информацию о любом пользователе.
        - Обычные пользователи могут получить информацию только о своем профиле.
        """
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
