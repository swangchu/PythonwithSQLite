# We should always close the database at the end of the program.
# we use CLOSE() method to close the database
# after which no code can access the database
# It is also for the security reasons


import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

# We have already the table if we run again, we may get an error
# So we have addedd IF NOT EXISTS in the query
cur.execute("CREATE TABLE IF NOT EXISTS studentInfo (rollNo INTEGER, name TEXT, class INTEGER)")

# We are going to insert two records in the studentInfo table
# Insert a record

cur.execute("INSERT INTO studentInfo VALUES (1, 'sonam', 12)")

#Insert another record in the table

cur.execute("INSERT INTO studentInfo VALUES (2, 'karma', 11)")

# SELECT IS A SQL COMMAND TO DISPLAY CONTENT OF THE TABLE IN DATABASE
# The wildcard * means all the columns of the record
# The query below will display all the columns and all the records
print("---------SELECT * ------------------------------------")
records = cur.execute("SELECT * FROM studentInfo").fetchall()
print("All the records in the table \n",records)

# SELECT A PARTICULAR RECORDS FROM DATABASE
# Lets get the record for a student with roll number 2
# WHERE in the SELECT statement filters the records 
print("-------SELECT WITH WHERE------------------------")
rollnumber2 = cur.execute("SELECT * FROM studentInfo WHERE rollno = 2").fetchall()
print("The roll number 2 is \n",rollnumber2)


# This method commits the current transaction. If you don’t call this 
# method, anything you did since the last call to commit() is not visible 
# from other database connections. If you wonder why you don’t see the data 
# you’ve written to the database, please check you didn’t forget to call 
# this method.

connection.commit()

# This closes the database connection. Note that this does not 
# automatically call commit(). If you just close your database connection without calling commit() 
# first, your changes will be lost!

connection.close()