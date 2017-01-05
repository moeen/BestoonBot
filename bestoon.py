#!/usr/bin/python
# -*- Coding: UTF-8 -*-

from telegram.ext import Updater,CommandHandler
from settings.conf import conf
import os, sys

class Bot_start():
    def __init__(self):
        self.token = conf.token()


    def main(self):
        os.system("clear")

        print "==============================="
        print "Starting Bestoon Bot!"
        print "==============================="
        print "Token\t\t\t:\t" + self.token

        if conf.configCheck() == "OK":
            print "Checking Config File\t:\t" + conf.configCheck()

        else:
            print "Checking Config File\t:\t" + conf.configCheck()
            sys.exit(0)

        print "Bestoon Bot Started, Now Let's Get To Work!"



if __name__ == "__main__":
    conf = conf()
    run = Bot_start()
    run.main()
    import bestoon.Plugins
