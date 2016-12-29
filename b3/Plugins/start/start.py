#!/usr/bin/python
# -*- Coding: UTF-8 -*-

from telegram.ext import Updater, CommandHandler

class starter():
    def __init__(self):
        self.updater = Updater("314422742:AAGHhiY7X0V2axzGdZz6dydEF1mcB8N_GJI")

    def start_method(self, bot, update):
        print "Log: start Method Executed"
        bot.sendMessage(update.message.chat_id, "Hello")
        self.start_command = CommandHandler("start", self.start_method)
        self.updater.dispatcher.add_handler(self.start_command)
