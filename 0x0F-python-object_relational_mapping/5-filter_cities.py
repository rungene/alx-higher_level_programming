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
    if len(args) != 5:
        print("Required: {} username password, db name ".format(arg[0]))
        exit(1)
    # get MyQL username, databasename and password as commandline args
    username = args[1]
    password = args[2]
    dbname = args[3]
    state_name = args[4]
    # connect to mysql sever on localhos, port 3306
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=dbname, port=3306)
    # cursor object
    cursor = db.cursor()
    # define an sql query with parameter from states name
    query = """SELECT cities.name FROM cities INNER JOIN\
            states ON cities.state_id = states.id WHERE\
            states.name = BINARY %s"""
    # execute the query with the state name parameter
    num_rows = cursor.execute(query, (state_name,))
    # fetch the rows iterate over them and print
    rows = cursor.fetchall()
    i = 1
    for row in rows:
        print(row[0], end='')
        if i < num_rows:
            print(end=', ')
        i += 1
        print()
    # close the cursor and db connections
    cursor.close()
    db.close()
