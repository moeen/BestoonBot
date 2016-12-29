#!/usr/bin/python
# -*- Coding: UTF-8 -*-

from telegram.ext import Updater
from b3.Plugins.start import start
from settings.conf import conf
from settings.sql import MySQL

import os
class b3_start():
    def __init__(self):
        try:
            conf = conf()
            print "try"
            self.db_host = conf.ConfigSectionMap("database", "b3/conf.ini")["host"].strip("\"")
            self.db_username = conf.ConfigSectionMap("database", "b3/conf.ini")["user"].strip("\"")
            self.db_password = conf.ConfigSectionMap("database", "b3/conf.ini")["password"].strip("\"")
            self.db_name = conf.ConfigSectionMap("database", "b3/conf.ini")["db_name"].strip("\"")
        except:
            print "exception"
            self.db_host = None
            self.db_username = None
            self.db_password = None
            self.db_name = None

    def main(self,token):
        os.system("clear")
        print self.db_host
        # print "==============================="
        # print "Starting Principal Bot"
        # print "Derived From Big Brother Bot"
        # print "==============================="
        # print "Token\t\t\t:\t" + token
        # print "Checking principal.conf\t:\t" + conf.configCheck()
        # print "Connecting To DB\t:\t" + MySQL.mysql_check(self.db_host, self.db_username, self.db_password, self.db_name)
        # print "Principal Bot Started, Now Let's Get To Work!"

        # starter = start.starter()
        # starter.start_method(bot, update)
        #
        # updater.start_polling()
        # updater.idle()


if __name__ == "__main__":
    conf = conf()
    print conf.ConfigSectionMap("database", "b3/conf.ini")["host"].strip("\"")
    run = b3_start()
    run.main("none")
