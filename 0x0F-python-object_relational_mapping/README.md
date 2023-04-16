# 0x0F. Python - Object-relational mapping

**Python OOP SQL MySQL ORM SQLAlchemy**

## Before you start…

Please make sure your MySQL server is in 8.0 -> [How to install MySQL 8.0 in Ubuntu 20.04](https://intranet.alxswe.com/projects/272)

## Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM). 

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

With an ORM:

```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right? 

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something. 

## Resources

**Read or watch:**

- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/) (please don’t pay attention to \_mysql)
- [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
- [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
- [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
- [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
- [10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/) (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

### General

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script 
- What ORM means
- How to map a Python Class to a MySQL table

### Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Your files will be executed with MySQLdb version 2.0.x
- Your files will be executed with SQLAlchemy version 1.4.x
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.\*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- You are not allowed to use execute with sqlalchemy

# More Info

## Install MySQLdb module version 2.0.x

For installing MySQLdb, you need to have MySQL installed: [How to install MySQL 8.0 in Ubuntu 20.04](https://intranet.alxswe.com/projects/272)

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

## Install SQLAlchemy module version 1.4.x

```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

Also, you can have this warning message:

```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
```

You can ignore it.

## Tasks

> 0. Get all states 

- Write a script that lists all states from the database hbtn_0e_0_usa: 

	- Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
	- You must use the module MySQLdb (import MySQLdb)
	- Your script should connect to a MySQL server running on localhost at port 3306
	- Results must be sorted in ascending order by states.id
	- Results must be displayed as they are in the example below
	- Your code should not be executed when imported

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**

**Repo:**

	- GitHub repository: alx-higher_level_programming
	- Directory: 0x0F-python-object_relational_mapping
	- File: 0-select_states.py

> 1. Filter states 

Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa: 

	- Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
	- You must use the module MySQLdb (import MySQLdb)
	- Your script should connect to a MySQL server running on localhost at port 3306
	- Results must be sorted in ascending order by states.id
	- Results must be displayed as they are in the example below
	- Your code should not be executed when imported

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```

**No test cases needed**

**Repo:**

	- GitHub repository: alx-higher_level_programming
	- Directory: 0x0F-python-object_relational_mapping
	- File: 1-filter_states.py

> 2. Filter states by user input 

Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

	- Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
	- You must use the module MySQLdb (import MySQLdb)
	- Your script should connect to a MySQL server running on localhost at port 3306
	- You must use format to create the SQL query with the user input
	- Results must be sorted in ascending order by states.id
	- Results must be displayed as they are in the example below
	- Your code should not be executed when imported

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**

**Repo:**

	- GitHub repository: alx-higher_level_programming
	- Directory: 0x0F-python-object_relational_mapping
	- File: 2-my_filter_states.py