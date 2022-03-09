# In 1_importConnection.py we have connected to the database.

# NOW WE WILL CREATE A TABLE IN THE DATABASE

import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()
# CREATE is a SQL command to create table.
# We are creating table named studentInfo
# with column name, rollNo whose data type is Integer, 
# name is Text and class is Integer

# Table name : studentInfo
# rollNo | name  | class

# execute() is method in the cursor that will execute the sql

cur.execute("CREATE TABLE studentInfo (rollNo INTEGER, name TEXT, class INTEGER)")



# run the code
# type python3 2_create.py in the terminal
# if nothing happens then your code run fine
# However, some unreadable data is added in the database.db 