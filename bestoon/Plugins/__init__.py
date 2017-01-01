#!/usr/bin/python
# -*- Coding : UTF-8 -*-

# PLEASE DEFINE YOUR `CommandHandler` AND `add_handler` OF EACH METHOD, RIGHT BELOW IT.
# PLEASE ADD YOUR PLUGINS INSIDE `extPlugins` AS I DON'T MERGE ANY THIRD PARTY PLUGINS INSIDE DEFAULT PLUGINS
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler
from settings.conf import conf

conf = conf()
updater = Updater(str(conf.token()))

def start_method(bot, update):
    """ Start Command """
    startList = [["Register New Account","Integrate A Registered Account"]]
    chat_id = update.message.chat_id
    text = """Hello And Welcome To [Bestoon](http://bestoon.ir).
This Bot Helps You Easily Access Your [Bestoon](http://bestoon.ir) Account.
Now, How Can I Help You?
"""
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id, text, parse_mode="Markdown", reply_markup=ReplyKeyboardMarkup(startList, one_time_keyboard=True))

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
