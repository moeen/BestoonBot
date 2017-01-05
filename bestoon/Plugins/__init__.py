#!/usr/bin/python
# -*- Coding : UTF-8 -*-

# PLEASE DEFINE YOUR `CommandHandler` AND `add_handler` OF EACH METHOD, RIGHT BELOW IT.
# PLEASE ADD YOUR PLUGINS INSIDE `extPlugins` AS I DON'T MERGE ANY THIRD PARTY PLUGINS INSIDE DEFAULT PLUGINS

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from settings.conf import conf
import os, sys

conf = conf()
updater = Updater(str(conf.token()))
SETUP, USERNAME, DUPLICATE, BESTOON, DONE = range(5)
info = []

def info_a():
    """ Writes User Data Into A File"""
    file_name = str(str(info[0])+".txt")
    with open ("bestoon/Plugins/users/%s" % file_name, mode="w") as f:
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
        user = update.message.from_user
        info.append(user.id)
        userfile = str(user.id) + ".txt"
        if os.path.isfile("bestoon/Plugins/users/%s" % userfile) == False:
            bot.sendChatAction(chat_id, "TYPING")
            register_text = """Ok.
Now Send Me Your Token.
"""
            update.message.reply_text(register_text,reply_markup=ReplyKeyboardRemove())
            return USERNAME
        else:
            List = [["Yes", "No"]]
            update.message.reply_text("It Seems This Telegram ID Has Been Integrated Before\nWould You Like To Integrate Again?",reply_markup=ReplyKeyboardMarkup(List))
            return DUPLICATE

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
    print txt
    print len(txt)
    if len(txt) == 48:
        print info
        info.append(txt)
        print "text appended"
        List = [["Finish"]]
        update.message.reply_text("Done! Now Send Me Finish To Send You Commands", reply_markup=ReplyKeyboardMarkup(List)),
        info_a()
        print "done!"
        return DONE
    else:
        update.message.reply_text("Sorry, This Token Is Invalid\nPlease Retry With A Valid Token.")

def remove_user(bot, update):
    text = update.message.text
    user = update.message.from_user
    if text.lower() == "yes":
        update.message.reply_text("Ok! Send Me New Token")
        print info
        return USERNAME
    elif text.lower() == "no":
        update.message.reply_text("Ok! Using Old Token!")
        return BESTOON

def cancel(bot, update):
    """ Cancel Command """
    bot.sendMessage(update.message.chat_id, "Bye!")
    return ConversationHandler.END
def done(bot, update):
    print "funv"
    # bot.sendChatAction(update.message.chat_id, "TEYPING")
    update.message.reply_text("You Can Now Use /income <value> and /expense <value> For Submiting Your Income And Expense.", reply_markup=ReplyKeyboardRemove())
    return BESTOON
def expense(bot, update):
    bot.sendMessage(update.message.chat_id, "expense")
def income(bot, update):
    bot.sendMessage(update.message.chat_id, "Income")

conv_handler = ConversationHandler(
    entry_points = [CommandHandler('start', start_method)],

    states = {
        SETUP: [MessageHandler(Filters.text, setup)],
        USERNAME: [MessageHandler(Filters.text, regUser)],
        DUPLICATE: [MessageHandler(Filters.text, remove_user)],
        DONE: [MessageHandler(Filters.text, done)],
        BESTOON: [CommandHandler("expense", expense),
        CommandHandler("income", income)]
    },

    fallbacks = [CommandHandler('start', start_method)]
)
updater.dispatcher.add_handler(conv_handler)
########## Starting Bot ##########
updater.start_polling()
updater.idle()
