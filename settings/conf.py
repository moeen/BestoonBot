#!/usr/bin/python
# -*- Coding: UTF-8 -*-

from telegram.ext import Updater
import ConfigParser
import os
class conf:
    def __init__(self):
        pass

    def ConfigSectionMap(self, section, config):
        self.Config = ConfigParser.ConfigParser()
        self.config_file = self.Config.read(config)

        self.dict1 = {}
        self.options = self.Config.options(section)
        for option in self.options:
            try:
                self.dict1[option] = self.Config.get(section, option)
                if self.dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                self.dict1[option] = None
        return self.dict1

    def configParser(self, section, address, config):
        return self.ConfigSectionMap(section,address)[config].strip("\"")

    def configCheck(self):
        if os.path.isfile("settings/conf.ini"):
            return "OK"
        else:
            return "FAILED"

    def token(self):
        self.token = self.configParser("bot", "settings/conf.ini", "updater")
        return self.token
