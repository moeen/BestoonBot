#!/usr/bin/python
# -*- Coding: UTF-8 -*-

import MySQLdb

class MySQL:
    def __init__(self):
        pass

    def mysql_check(self, host, user, password, db_name):
        try:
            db = MySQLdb.connect(host=host, user=user, passwd=password, db=db_name)
            cursor = db.cursor()

            if cursor.execute("SELECT * FROM information_schema.tables WHERE TABLE_NAME = 'users' AND TABLE_SCHEMA=\'%s\' ;" % db_name) == 0:
                cursor.execute("USE " + db_name + ";"\
                    + "CREATE TABLE IF NOT EXISTS`users` ("\
                    + "`id` int(10) unsigned NOT NULL AUTO_INCREMENT,"\
                    + "`tg_id` int(10) unsigned NOT NULL,"\
                    + "`token` varchar(45) NOT NULL,"\
                    + "PRIMARY KEY (`id`)"\
                    + ") ENGINE=InnoDB DEFAULT CHARSET=latin1;"\
                    + "LOCK TABLES `users` WRITE;"\
                    + "UNLOCK TABLES;")
            db.commit()
            db.close()
            return "OK"
        except:
            return "FAILED"
    def sql_query(self, host, user, password, db_name, query):
        try:
            db = MySQLdb.connect(host=host, user=user, passwd=password, db=db_name)
            cursor = db.cursor()
            cursor.execute(query)
            db.commit()
            db.close()

        except:
            print "Error Executing Query In sql.py: sql_query()."
