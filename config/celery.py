from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Импорт настроек Celery из настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Подключение всех задач celery из всех приложений
app.autodiscover_tasks()
