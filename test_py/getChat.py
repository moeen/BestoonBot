#!/usr/bin/python
# -*- Coding: UTF-8 -*-

from telegram.ext import CommandHandler, Updater

updater = Updater("314422742:AAGHhiY7X0V2axzGdZz6dydEF1mcB8N_GJI")

def getChats(bot, update):
    chat_id = update.message.chat_id
    userinf = update.message.from_user
    if str(userinf.id) == "130162558":
        bot.sendChatAction(chat_id, "TYPING")
        bot.sendMessage(chat_id, "Baz In Mamad Azizi Oomad, GOLESH KHIAAREEEEE!")
    else:
        bot.sendChatAction(chat_id, "TYPING")
        bot.sendMessage(chat_id, "Chat ID: " + str(userinf.id) + "\nUserName: " + str(userinf.username) + "\nFirst Name: " + str(userinf.first_name) + "\nLast Name: " + str(userinf.last_name))
    print bot.getChat(chat_id)
    print "========="
    print userinf
    print "========="
    print bot.getChatMembersCount(chat_id)

def group_info(bot, update):
    print "Info Executed"
    chat_id = update.message.chat_id
    userinf = update.message.from_user
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id,"Active Members: " + str(bot.getChatMembersCount(chat_id)))

def kick_member(bot, update, args):
    print "User Kick Requested."
    chat_id = update.message.chat_id
    userinf = update.message.from_user
    if str(userinf.id) == "140301737":
        if str(args[0]) == "140301737":
            bot.sendMessage(chat_id, "@AlirezaieS Owns You! Can't Kick.")
        else:
            bot.sendMessage(chat_id, "Kicking: " + str(args[0] + " Requested! "))
            bot.kickChatMember(chat_id, args[0])
    else:
        bot.sendChatAction(chat_id, "TYPING")
        bot.sendMessage(chat_id, str(userinf.first_name) + "Bitch, You Wanna Kick? Lick My Balls")

def bye_bye(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id,"Bot Is Shutting Down, Bye Bye Fucking Noobs! \n Golesh Khiareee!!")
    exit()

def leave(bot, update):
    chat_id = update.message.chat_id
    user = update.message.from_user
    if str(user.username) == "AlirezaieS":

        bot.sendChatAction(chat_id, "TYPING")
        bot.sendMessage(chat_id, "I'm Leaving This Shit, You All Fucking Noobs Can Suck My Dick!")
        bot.leaveChat(-1001090294252)
    else:
        bot.sendChatAction(chat_id, "TYPING")
        bot.sendMessage(chat_id, "Lick My Balls Bitch, You Are Not Admin.")

def get_member(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id, str(bot.getChatMember(chat_id, 140301737)))

def weed(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    userinf = update.message.from_user
    if str(userinf.id) == "130162558":
        bot.sendMessage(chat_id, "Lick My Balls Mamad Azizi")
    elif str(userinf.id) == "140301737":
        bot.sendMessage(chat_id, "Some One Call #Bob_Marley And He Bring @AlirezaieS 420 Grams OF Afghan Kush")
    else:
        bot.sendMessage(chat_id,"Yala Kooniaaaaa Berim Gol Beigiriiiiiiim!")

def olala(bot, update, args):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id, "Awwwww La La, Sexy " + str(args[0]))

def kooni(bot, update, args):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id, str(args[0]) + " Is The Biggest K00ni Of The World!")

getChats_command = CommandHandler("start", getChats)
info_command = CommandHandler("info", group_info)
bye_command = CommandHandler("bye_bye",bye_bye)
kick_command = CommandHandler("kick", kick_member,pass_args=True)
leave_command = CommandHandler("leave", leave)
member_command = CommandHandler("members", get_member)
weed_command = CommandHandler("weed", weed)
olala_command = CommandHandler("olala", olala, pass_args=True)
kooni_command = CommandHandler("kooni", kooni, pass_args=True)

updater.dispatcher.add_handler(kooni_command)
updater.dispatcher.add_handler(olala_command)
updater.dispatcher.add_handler(weed_command)
updater.dispatcher.add_handler(member_command)
updater.dispatcher.add_handler(leave_command)
updater.dispatcher.add_handler(bye_command)
updater.dispatcher.add_handler(kick_command)
updater.dispatcher.add_handler(info_command)
updater.dispatcher.add_handler(getChats_command)

updater.start_polling()
updater.idle()
