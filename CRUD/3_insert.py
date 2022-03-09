# HERE WE ARE GOING TO INSERT SOME DATA IN THE TABLE WE HAVE CREATED
# IN 2_create.py

import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

# We have already the table if we run again, we may get an error
# So we have addedd IF NOT EXISTS in the query
cur.execute("CREATE TABLE IF NOT EXISTS studentInfo (rollNo INTEGER, name TEXT, class INTEGER)")

# We are going to insert two records in the studentInfo table
# Insert a record

# INSERT IS A SQL COMMAND TO ENTERED RECORDS IN THE TABLE

cur.execute("INSERT INTO studentInfo VALUES (1, 'sonam', 12)")

#Insert another record in the table

cur.execute("INSERT INTO studentInfo VALUES (2, 'karma', 11)")

# run the code
# type python3 3_insert.py in the terminal
# if nothing happens then your code run fine
# However, some unreadable data is added in the database.db 