FROM python:3.10.14-bullseye

WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Создаем виртуальное окружение, активируем его и устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы проекта в рабочую директорию контейнера
COPY . .

# Указываем команду для запуска приложения
CMD [sh, /app/entrypoint.sh]