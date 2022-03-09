# sqlite3 module comes along with the python bundle so there is no need to install 
# to use it we need to import the sqlite3 module 
# import sqlite3 gives our Python program access to the sqlite3 module. 

# This statement is required

import sqlite3

# The sqlite3.connect() function returns a Connection object that we will use to interact 
# with the SQLite database held in the file database.db.
# The database file name can be any name

# This statement is required

connection = sqlite3.connect('database.db')

# Cursor objects allow us to send SQL statements 
# to a SQLite database using cursor.execute().

# This statement is required
cur = connection.cursor()

# run the program
# python3 1_importConnection.py

# if nothing happens then your program worked fine
# However, in the current folder database (database.db) file will be created.



