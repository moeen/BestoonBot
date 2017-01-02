#!/usr/bin/python
# -*- Coding : UTF-8 -*-

# PLEASE DEFINE YOUR `CommandHandler` AND `add_handler` OF EACH METHOD, RIGHT BELOW IT.
# PLEASE ADD YOUR PLUGINS INSIDE `extPlugins` AS I DON'T MERGE ANY THIRD PARTY PLUGINS INSIDE DEFAULT PLUGINS
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from settings.conf import conf

conf = conf()
updater = Updater(str(conf.token()))
SETUP , REGISTER, INTEGRATE = range(3)
def start_method(bot, update):
    """ Start Command """

    startList = [["Register New Account","Integrate A Registered Account"]]

    chat_id = update.message.chat_id
    replyText = update.message.text

    text = """Hello And Welcome To [Bestoon](http://bestoon.ir).
This Bot Helps You Easily Access Your [Bestoon](http://bestoon.ir) Account.
Now, How Can I Help You?
"""
    bot.sendChatAction(chat_id, "TYPING")
    update.message.reply_text(text, parse_mode="Markdown",reply_markup=ReplyKeyboardMarkup(startList, one_time_keyboard=True))
    return SETUP

def setup(bot, update):
    """Initialize The User Account For The First Time"""
    chat_id = update.message.chat_id

    if update.message.text == "Register New Account":
        bot.sendChatAction(chat_id, "TYPING")
        update.message.reply_text("Can\'t Register Now!")

    elif update.message.text == "Integrate A Registered Account":
        bot.sendChatAction(chat_id, "TYPING")
        update.message.reply_text("Can\'t Integrate Now!")

def bye(bot, update):
    bot.sendMessage(update.message.chat_id, "bye!")

conv_handler = ConversationHandler(
    entry_points = [CommandHandler('start', start_method)],

    states = {
        SETUP: [MessageHandler(Filters.text, setup)]

    },

    fallbacks = [CommandHandler('cancel', bye)]
)
updater.dispatcher.add_handler(conv_handler)
########## Starting Bot ##########
updater.start_polling()
updater.idle()
