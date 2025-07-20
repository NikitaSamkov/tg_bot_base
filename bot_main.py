# -*- coding: utf-8 -*-
__author__ = "Самков Н.А. https://github.com/NikitaSamkov"
__maintainer__ = "Самков Н.А. https://github.com/NikitaSamkov"
__doc__ = "Основной модель для запуска бота"

from telegram.ext import Updater
from settings import get_settings


bot_settings = get_settings()


def main():
    updater = Updater(bot_settings.get('BOT', 'BOT_TOKEN'), use_context=True)
    dp = updater.dispatcher


if __name__ == '__main__':
    main()
