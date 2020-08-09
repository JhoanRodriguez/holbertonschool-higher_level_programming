#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    STATE_NAME = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == STATE_NAME:
            print(row)
    cur.close()
    db.close()
