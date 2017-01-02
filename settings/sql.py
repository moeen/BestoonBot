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
                    + "`username` varchar(45) NOT NULL,"\
                    + "`email` varchar(45) NOT NULL,"\
                    + "`token` varchar(45) NOT NULL,"\
                    + "`password` varchar(45) NOT NULL,"\
                    + "PRIMARY KEY (`id`)"\
                    + ") ENGINE=InnoDB DEFAULT CHARSET=latin1;"\
                    + "LOCK TABLES `users` WRITE;"\
                    + "UNLOCK TABLES;")

            return "OK"
        except:
            return "FAILED"
#INSERT INTO `bestoon`.`users` (`id`, `tg_id`, `username`, `email`, `token`, `password`) VALUES ('1', '140301737', 'AlirezaieS', 'alirezaie.sadegh@gmail.com', '3YS4fVd1iuTZfS2lX3Z6nQYMFKos9GjaWSH0oEdneEzElLt2', 'AssH0l3');
#INSERT INTO `bestoon`.`users` (`tg_id`, `username`, `email`, `token`, `password`) VALUES ('140301737', 'AlirezaieS', 'alirezaie.sadegh@gmail.com', '3YS4fVd1iuTZfS2lX3Z6nQYMFKos9GjaWSH0oEdneEzElLt2', 'AssH0l3');

    def sql_query(self, host, user, password, db_name, query):
        try:
            db = MySQLdb.connect(host=host, user=user, passwd=password)
            cursor = db.cursor()
            cursor.execute(query)
        except:
            print "Error Executing Query In sql.py: sql_query()."
