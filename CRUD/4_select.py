# We have inserted two records in the table using the 2_create.py

# HERE WE WILL DISPLAY THE RECORDS ENTERED IN THE TABLE

import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

# We have already the table if we run again, we may get an error
# So we have addedd IF NOT EXISTS in the query
cur.execute("CREATE TABLE IF NOT EXISTS studentInfo (rollNo INTEGER, name TEXT, class INTEGER)")

# We are going to insert two records in the studentInfo table
# Insert a record

#cur.execute("INSERT INTO studentInfo VALUES (1, 'sonam', 12)")

#Insert another record in the table

#cur.execute("INSERT INTO studentInfo VALUES (2, 'karma', 11)")

# SELECT IS A SQL COMMAND TO DISPLAY CONTENT OF THE TABLE IN DATABASE
# The wildcard * means all the columns of the record
# The query below will display all the columns and all the records

records = cur.execute("SELECT * FROM studentInfo").fetchall()
print("All the records in the table \n",records)

# run the code
# type python3 3_insert.py in the terminal
# You will get all the records in the database