#!/usr/bin/python
# -*- Coding: UTF-8 -*-

import MySQLdb

class MySQL:
    def __init__(self):
        pass

    def mysql_check(self, host, user, password, db_name):
        try:
            self.db = MySQLdb.connect(host=host, user=user, passwd=password)
            self.cursor = db.cursor()
            self.cursor.execute("USE " + db_name + ";" \
                + "CREATE TABLE IF NOT EXISTS`group` (`join_status` int(10) unsigned NOT NULL,`sticker` int(10) unsigned NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;"\
                + "LOCK TABLES `group` WRITE;"\
                + "UNLOCK TABLES;"\
                + "CREATE TABLE IF NOT EXISTS `users`("\
                + "`id` int(10) unsigned NOT NULL AUTO_INCREMENT,"\
                + "`chatid` int(10) unsigned NOT NULL,"\
                + "`username` varchar(45) COLLATE utf8_persian_ci DEFAULT NULL,"\
                + "`firstname` varchar(45) COLLATE utf8_persian_ci DEFAULT NULL,"\
                + "`lastname` varchar(45) COLLATE utf8_persian_ci DEFAULT NULL,"\
                + "`warns` int(10) unsigned NOT NULL DEFAULT '0',"\
                + "`kicks` int(10) unsigned NOT NULL DEFAULT '0',"\
                + "`ban_status` int(10) unsigned NOT NULL DEFAULT '0',"\
                + "`user_activity` int(10) unsigned NOT NULL DEFAULT '1',"\
                + "`aliases` varchar(45) COLLATE utf8_persian_ci DEFAULT NULL,"\
                + "`level` int(10) unsigned NOT NULL DEFAULT '1',"\
                + "PRIMARY KEY (`id`)"
                + ")"\
                + "ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;"\
                + "LOCK TABLES `users` WRITE;"\
                + "UNLOCK TABLES;")

            return "OK"

        except:
            return "FAILED"

    def sql_query(self, host, user, password, db_name, query):
        try:
            db = MySQLdb.connect(host=host, user=user, passwd=password)
            cursor = db.cursor()
            cursor.execute(query)
        except:
            print "Error Executi Query."
