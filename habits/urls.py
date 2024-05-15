from django.urls import path
from .views import HabitViewSet

urlpatterns = [
    path('habits/', HabitViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='habit-list'),
    path('habits/public/', HabitViewSet.as_view({
        'get': 'list_public'
    }), name='public-habit-list'),
    path('habits/<int:pk>/', HabitViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='habit-detail'),
]
