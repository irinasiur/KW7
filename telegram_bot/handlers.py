from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    """Отправляет сообщение при команде /start."""
    update.message.reply_text('Привет! Я твой бот-напоминатель для привычек.')


def help_command(update: Update, context: CallbackContext):
    """Отправляет сообщение с описанием возможностей бота при команде /help."""
    update.message.reply_text('Отправьте /start для начала работы с ботом.')


def error_handler(update: Update, context: CallbackContext):
    """Логирует ошибки."""
    print(f'Update {update} caused error {context.error}')
