#!/usr/bin/python
# -*- Coding: UTF-8 -*-

import MySQLdb

def db_query(query):
    db = MySQLdb.connect(host=host, user=user, passwd=password)
    cursor = db.cursor()
    cursor.execute(query)
