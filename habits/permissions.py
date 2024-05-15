from rest_framework import permissions


class IsOwnerOrPublicReadOnly(permissions.BasePermission):
    """
    Право доступа, которое разрешает пользователям взаимодействовать только со своими привычками для операций CRUD.
    Все пользователи, включая неавторизованных, могут просматривать публичные привычки, но не могут их редактировать или удалять.
    """

    def has_object_permission(self, request, view, obj):
        # Проверки на методы чтения
        if request.method in permissions.SAFE_METHODS:
            # Если привычка публичная, разрешаем просмотр
            if obj.is_public:
                return True
            # Если привычка принадлежит пользователю, разрешаем просмотр
            if obj.user == request.user:
                return True
        # Для операций изменения, удаления проверяем, что пользователь является владельцем привычки
        return obj.user == request.user

    def has_permission(self, request, view):
        # Для операций создания нужно быть аутентифицированным пользователем
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        return True


class IsSelfOrAdmin(permissions.BasePermission):
    """
    Пользователи могут редактировать только свой собственный профиль, а администраторы имеют доступ ко всем профилям.
    """

    def has_object_permission(self, request, view, obj):
        # Администраторы могут видеть любой профиль
        if request.user.is_staff:
            return True
        # Пользователи могут видеть и редактировать только свой профиль
        return obj == request.user
