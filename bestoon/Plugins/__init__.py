#!/usr/bin/python
# -*- Coding : UTF-8 -*-

# PLEASE DEFINE YOUR `CommandHandler` AND `add_handler` OF EACH METHOD, RIGHT BELOW IT.
# PLEASE ADD YOUR PLUGINS INSIDE `extPlugins` AS I DON'T MERGE ANY THIRD PARTY PLUGINS INSIDE DEFAULT PLUGINS

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from settings.conf import conf

conf = conf()
updater = Updater(str(conf.token()))
SETUP ,USERNAME = range(2)
info = []

def info_a():
    """ Writes User Data Into A File"""
    file_name = str(str(info[0])+".txt")
    with open ("bestoon/Plugins/tmp/%s" % file_name, mode="w") as f:
        f.write(str(info[0]) + "," + str(info[1]))
        f.close()

def start_method(bot, update):
    """ Start Command """
    startList = [["Register New Account","Integrate An Account"]]

    global chat_id
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
    if update.message.text == "Integrate An Account":
        info.append(update.message.from_user.id)
        bot.sendChatAction(chat_id, "TYPING")
        register_text = """Ok.
Now Send Me Your Token.
"""
        update.message.reply_text(register_text,reply_markup=ReplyKeyboardRemove())
        return USERNAME

    elif update.message.text == "Register New Account":
        bot.sendChatAction(chat_id, "TYPING")
        update.message.reply_text("Sorry, Can\'t Integrate Now!", reply_markup=ReplyKeyboardRemove())
        bot.sendMessage(update.message.chat_id, "Bye!")
        return ConversationHandler.END

    else:
        bot.sendChatAction(chat_id, "TYPING")
        update.message.reply_text("Invalid Command!")

def regUser(bot, update):
    txt = update.message.text
    if len(str(txt)) == 48:
        info.append(update.message.text.lower())
        update.message.reply_text("Processing Your Request,Please Wait.")
        info_a()
    else:
        update.message.reply_text("Sorry, This Token Is Invalid\nPlease Retry With A Valid Token.")


def cancel(bot, update):
    """ Cancel Command """
    bot.sendMessage(update.message.chat_id, "Bye!")
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points = [CommandHandler('start', start_method)],

    states = {
        SETUP: [MessageHandler(Filters.text, setup)],
        USERNAME: [MessageHandler(Filters.text, regUser)]

    },

    fallbacks = [CommandHandler('cancel', cancel)]
)
updater.dispatcher.add_handler(conv_handler)
########## Starting Bot ##########
updater.start_polling()
updater.idle()
