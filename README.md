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


# Django проект с Docker, Celery, Redis и Swagger

Этот проект также является Django приложением, контейнеризованным с использованием Docker. Он включает Celery для асинхронных задач, Redis в качестве брокера сообщений и Swagger для документации API.

## Предварительные требования

- Установленные Docker и Docker Compose.
- Python и pip (для локальной разработки).

## Настройка проекта

1. **Клонирование репозитория:**

    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Создание и настройка файла `.env`:**

    Создайте файл `.env` в корневом каталоге проекта и добавьте в него следующие переменные окружения:

    ```plaintext
    # Настройки Django
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1

    # Настройки базы данных
    POSTGRES_NAME=habits
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=q1
    POSTGRES_HOST=habits
    POSTGRES_PORT=5432

    # Настройки Redis
    REDIS_HOST=redis
    REDIS_PORT=6379
    REDIS_DB=0
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_TIMEZONE=Europe/Moscow
    TIME_ZONE=UTC

    # Настройки CORS
    CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
    ```

3. **Сборка и запуск контейнеров Docker:**

    ```sh
    docker-compose up --build
    ```

    Эта команда соберет образы Docker и запустит контейнеры. Приложение будет доступно по адресу `http://localhost:8000`.

4. **Применение миграций базы данных:**

    В новом терминале выполните команду:

    ```sh
    docker-compose exec app python manage.py migrate
    ```

5. **Создание суперпользователя (опционально, для доступа к административному интерфейсу Django):**

    ```sh
    docker-compose exec app python manage.py createsuperuser
    ```

## Доступ к приложению

- **Django приложение:** `http://localhost:8000`
- **Административный интерфейс:** `http://localhost:8000/admin`
- **Документация Swagger:** `http://localhost:8000/swagger/`

## Запуск задач Celery

Celery и Celery Beat уже настроены и работают как отдельные сервисы в Docker. Вы можете определять свои задачи в файлах `tasks.py` ваших Django приложений.

## Остановка приложения

Для остановки приложения и удаления контейнеров выполните команду:

```sh
docker-compose down -v



