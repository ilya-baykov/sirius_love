from os import environ

from aiogram import Dispatcher, Bot

from app.handlers.start.registration import register_start_handlers
from app.handlers.unknow_command.unknow_response import register_unknown_command

dp = Dispatcher()
bot = Bot(token=environ.get('TOKEN', 'define me!'))


async def start_bot():
    # Регистрация обработчиков

    register_start_handlers(dp)  # Стартовый обработчик
    register_unknown_command(dp)  # Обработчик неизвестных команд

    await dp.start_polling(bot, skip_updates=True)
