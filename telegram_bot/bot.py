from telegram.ext import Updater, CommandHandler
from .handlers import start, error_handler, help_command
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    TOKEN = os.getenv('TELEGRAM_TOKEN')
    updater = Updater(token=TOKEN, use_context=True)

    # Диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрация обработчиков
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_error_handler(error_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
