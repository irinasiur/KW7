# Habit Tracker

Этот проект представляет собой трекер привычек, разработанный с использованием Django и Django REST Framework. Приложение позволяет пользователям создавать, редактировать и отслеживать свои привычки. Также реализована интеграция с Telegram для отправки уведомлений и поддержка отложенных задач через Celery.

## Установка

### Клонирование репозитория

```bash
git clone https://github.com/ваш-аккаунт-на-гитхабе/habit-tracker.git
cd habit-tracker
```

### Создание виртуального окружения
```bash
python -m venv env
source env/bin/activate  # для Windows: env\Scripts\activate
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Настройка переменных окружения
Создайте файл .env в корне проекта и добавьте следующие переменные:

```
SECRET_KEY=ваш-секретный-ключ
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
TELEGRAM_TOKEN=ваш-токен-telegram
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_TIMEZONE=Europe/Moscow
TIME_ZONE=UTC
DB_NAME=ваше-имя-базы-данных
DB_USER=ваш-пользователь-базы-данных
DB_PASSWORD=ваш-пароль-базы-данных
DB_HOST=localhost
DB_PORT=5432
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### Применение миграций
```bash
python manage.py migrate
```

### Создание суперпользователя
```bash
python manage.py createsuperuser
```

### Запуск сервера разработки
```bash
python manage.py runserver
```

### Запуск Celery
В отдельном терминале запустите Celery:
```bash
celery -A config worker --loglevel=info
```

### Запуск Celery Beat
В отдельном терминале запустите Celery Beat:
```bash
celery -A config beat --loglevel=info
```

### Тестирование
Для запуска тестов используйте команду:
```bash
pytest
```

## Документация API

Документация API доступна по следующим URL-адресам после запуска сервера разработки:

- Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Redoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## Основные эндпоинты

- Регистрация пользователя: `/users/register/`
- Авторизация: `/users/login/`
- Обновление токена: `/users/login/refresh/`
- Управление привычками: `/habits/`
- Публичные привычки: `/habits/public/`

## Структура проекта

- `config/` - Настройки и конфигурации проекта.
- `users/` - Приложение для управления пользователями.
- `habits/` - Приложение для управления привычками.
- `telegram_bot/` - Интеграция с Telegram для отправки уведомлений.
- `tests/` - Тесты для приложения.


