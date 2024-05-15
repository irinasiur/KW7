from celery import shared_task
from dotenv import load_dotenv
from telegram import Bot
import os

# Загрузите переменные окружения из .env файла
load_dotenv()


@shared_task
def send_telegram_reminder(user_id, message):
    # Здесь код для отправки уведомления через Telegram
    TOKEN = os.getenv('TELEGRAM_TOKEN')
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=user_id, text=message)
