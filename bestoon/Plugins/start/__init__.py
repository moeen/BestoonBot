# #!/usr/bin/python
# # -*- Coding : UTF-8 -*-

from telegram.ext import Updater, CommandHandler
from settings.conf import conf

print "Start Plugin Imported"

conf = conf()
updater = Updater(str(conf.token()))

def start_method(bot, update):
    print "start Executed"
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id, "Hello")

start_command = CommandHandler("start", start_method)
updater.dispatcher.add_handler(start_command)

print "Start Plugin Ends Here"
