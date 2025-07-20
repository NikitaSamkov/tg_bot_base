# -*- coding: utf-8 -*-
__author__ = "Самков Н.А. https://github.com/NikitaSamkov"
__maintainer__ = "Самков Н.А. https://github.com/NikitaSamkov"
__doc__ = "Команды бота"

from telegram import Update
from telegram.ext import CallbackContext
from logs import log_msg
from security import is_admin, is_in_whitelist


def command_common(func):
    """Общий декоратор для команд бота"""
    def wrapper(update: Update, context: CallbackContext):
        user_info = update.message.from_user
        log_msg(f'{user_info.full_name} (@{user_info.username}) - {update.message.text}')
        return func(update, context)
    return wrapper


def admin_only(func):
    """Декоратор проверки на администратора"""
    def wrapper(update: Update, context: CallbackContext):
        if not is_admin(update.message.from_user.id):
            return update.message.reply_text('У вас недостаточно прав для вызова этой команды!')
        return func(update, context)
    return wrapper


def whitelist_only(func):
    """Декоратор проверки на нахождение пользователя в белом списке"""
    def wrapper(update: Update, context: CallbackContext):
        if not is_in_whitelist(update.message.from_user.id):
            return update.message.reply_text('У вас недостаточно прав для вызова этой команды!')
        return func(update, context)
    return wrapper


@command_common
def start_comm(update: Update, context: CallbackContext) -> None:
    """Команда start"""
    update.message.reply_text("""
Привет! Я умею работать со следующими командами:
/start - Показывает текущее сообщение
""")
