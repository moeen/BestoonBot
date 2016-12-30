#!/usr/bin/python
# -*- Coding : UTF-8 -*-
#TODO: Fix The Token Access (Token Sould Easily Accessed By settings.cinf.token())

from settings.conf import conf
from telegram.ext import Updater, CommandHandler
updater = Updater(conf.token())
def start_method(bot, update):
    bot.sendMessage(update.message.chat_id, "Hello")

start_command = CommandHandler("start", start_method)
updater.dispatcher.add_handler(start_command)
