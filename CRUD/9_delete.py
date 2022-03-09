# We have inserted two records in the table using the 2_create.py

# HERE WE WILL DISPLAY PARTICULAR RECORDS ENTERED IN THE TABLE

import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

# We have already the table if we run again, we may get an error
# So we have addedd IF NOT EXISTS in the query
cur.execute("CREATE TABLE IF NOT EXISTS studentInfo (rollNo INTEGER, name TEXT, class INTEGER)")

# We are going to insert two records in the studentInfo table
# Insert a record

"""cur.execute("INSERT INTO studentInfo VALUES (1, 'sonam', 12)")"""

#Insert another record in the table

"""cur.execute("INSERT INTO studentInfo VALUES (2, 'karma', 11)")"""

# SELECT IS A SQL COMMAND TO DISPLAY CONTENT OF THE TABLE IN DATABASE
# The wildcard * means all the columns of the record
# The query below will display all the columns and all the records
"""
print("---------SELECT * ------------------------------------")
records = cur.execute("SELECT * FROM studentInfo").fetchall()
print("All the records in the table \n",records)
"""
# SELECT A PARTICULAR RECORDS FROM DATABASE
# Lets get the record for a student with roll number 2
# WHERE in the SELECT statement filters the records 
"""
print("-------SELECT WITH WHERE------------------------")
rollnumber2 = cur.execute("SELECT * FROM studentInfo WHERE rollno = 2").fetchall()
print("The roll number 2 is \n",rollnumber2)
"""

# THERE WOULD BE A TIME WHERE WE MAY HAVE TO MAKE CHANGES TO THE RECORDS ADDED TO
# THE DATABASE TABLE. SQLITE USES UPDATE COMMAND TO MAKE CHANGES TO THE RECORDS

# Roll number 2 in the record is karma, we want to change to wangchu
# Lets change it using the code below
"""
cur.execute("UPDATE studentInfo SET name = 'Wangchu' WHERE rollno = 2")
"""

# Lets get the record with roll no 2 and print it
"""
print("-------SELECT WITH WHERE ROLL NO is 2------------------------")
rollnumber2 = cur.execute("SELECT * FROM studentInfo WHERE rollno = 2").fetchall()
print("The updated record for roll number 2 is \n",rollnumber2)
"""

# DELETE COMMAND IN SQLITE
# DELETE SQL statement to remove the rocord from the table
# Lets delete roll number 1 from the database

cur.execute("DELETE FROM studentInfo WHERE rollno=1")

#Lets see whether the record is deleted or not from the database
# for that we will have to use SELECT to display all the records in the database

print("-------SELECT ALL RECORDS IN DB------------------------")
records = cur.execute("SELECT * FROM studentInfo").fetchall()
print("Latest records in the database is \n",records)


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