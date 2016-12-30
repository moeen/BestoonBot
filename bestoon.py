#!/usr/bin/python
# -*- Coding: UTF-8 -*-

from telegram.ext import Updater
from settings.conf import conf
from settings.sql import MySQL
import os
from bestoon import *
class Bot_start():
    def __init__(self):
        self.token = conf.token()

        try:
            self.db_host = conf.ConfigSectionMap("database", "settings/conf.ini")["host"].strip("\"")
            self.db_username = conf.ConfigSectionMap("database", "settings/conf.ini")["user"].strip("\"")
            self.db_password = conf.ConfigSectionMap("database", "settings/conf.ini")["password"].strip("\"")
            self.db_name = conf.ConfigSectionMap("database", "settings/conf.ini")["db_name"].strip("\"")
        except:
            print "exception"
            self.db_host = None
            self.db_username = None
            self.db_password = None
            self.db_name = None

    def main(self):
        os.system("clear")
        mysql = MySQL()
        print "==============================="
        print "Starting Bestoon Bot!"
        print "==============================="
        print "Token\t\t\t:\t" + self.token
        print "Checking principal.conf\t:\t" + conf.configCheck()
        print "Connecting To DB\t:\t" + mysql.mysql_check(self.db_host, self.db_username, self.db_password, self.db_name)
        print "Bestoon Bot Started, Now Let's Get To Work!"
        updater = Updater(self.token)
        updater.start_polling()
        updater.idle()


if __name__ == "__main__":
    conf = conf()
    run = Bot_start()
    run.main()
