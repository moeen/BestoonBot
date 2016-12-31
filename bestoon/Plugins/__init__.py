#!/usr/bin/python
# -*- Coding : UTF-8 -*-

from telegram.ext import Updater, CommandHandler
from settings.conf import conf

conf = conf()
updater = Updater(str(conf.token()))

def start_method(bot, update):
    """ Start Command """
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id, "Hello")

def bye_method(bot, update):
    """ Start Command """
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id, "Goodbye!")

########## Define Commands Here ##########
goodbye_command = CommandHandler("bye", bye_method)
start_command = CommandHandler("start", start_method)
updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(goodbye_command)

########## Starting Bot ##########
updater.start_polling()
updater.idle()
