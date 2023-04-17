#!/usr/bin/python3
"""
 lists all states with a name starting with N
 (upper N) from the database hbtn_0e_0_usa:

author: Clevers Rungene
"""
import MySQLdb
import sys
if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Required: {} username password, db name ".format(arg[0]))
        exit(1)
    # get MyQL username, databasename and password as commandline args
    username = args[1]
    password = args[2]
    dbname = args[3]
    # connect to mysql sever on localhos, port 3306
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=dbname, port=3306)
    # cursor object
    cursor = db.cursor()
    # sql query to retrive all cities and sort results by city id
    cursor.execute("SELECT cities.id, cities.name, states.name FROM \
                    cities INNER JOIN states ON cities.state_id = \
                    states.id ORDER \
                    BY cities.id ASC")
    # fetch the rows iterate over them and print
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # close the cursor and db connections
    cursor.close()
    db.close()
