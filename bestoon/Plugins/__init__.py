#!/usr/bin/python
# -*- Coding : UTF-8 -*-

# PLEASE DEFINE YOUR `CommandHandler` AND `add_handler` OF EACH METHOD, RIGHT BELOW IT.
# PLEASE ADD YOUR PLUGINS INSIDE `extPlugins` AS I DON'T MERGE ANY THIRD PARTY PLUGINS INSIDE DEFAULT PLUGINS

from telegram.ext import Updater, CommandHandler
from settings.conf import conf

conf = conf()
updater = Updater(str(conf.token()))

def start_method(bot, update):
    """ Start Command """
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id, "Hello")

start_command = CommandHandler("start", start_method)
updater.dispatcher.add_handler(start_command)

def bye_method(bot, update):
    """ Goodbye Command """
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id, "Goodbye!")

goodbye_command = CommandHandler("bye", bye_method)
updater.dispatcher.add_handler(goodbye_command)

########## Starting Bot ##########
updater.start_polling()
updater.idle()
