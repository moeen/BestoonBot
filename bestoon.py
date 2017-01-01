#!/usr/bin/python
# -*- Coding: UTF-8 -*-
#TODO: Running Plugins Easily Inside This File
from telegram.ext import Updater,CommandHandler
from settings.conf import conf
from settings.sql import MySQL
import os, sys

class Bot_start():
    def __init__(self):
        self.token = conf.token()
        self.flag =[]

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

        if conf.configCheck() == "OK":
            print "Checking principal.conf\t:\t" + conf.configCheck()
        else:
            print "Checking principal.conf\t:\t" + conf.configCheck()
            sys.exit(0)

        sql_check = mysql.mysql_check(self.db_host, self.db_username, self.db_password, self.db_name)

        if sql_check == "OK":
            print "Connecting To DB\t:\t" + sql_check
        else:
            print "Connecting To DB\t:\t" + sql_check
            sys.exit(0)

        print "Bestoon Bot Started, Now Let's Get To Work!"



if __name__ == "__main__":
    conf = conf()
    run = Bot_start()
    run.main()
    import bestoon.Plugins
