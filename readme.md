# Python with SQLite

**What is database ?**

    According to https://www.oracle.com/database/what-is-database/
    
    A database is an organized collection of structured information, or data, typically stored electronically in a computer system. 
    A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS,along with the applications 
    that are associated with them, are referred to as a database system, often shortened to just database.

    Data within the most common types of databases in operation today is typically modeled in rows and columns in a series of tables to 
    make processing and data querying efficient. The data can then be easily accessed, managed, modified, updated, controlled, and organized. 
    Most databases use structured query language (SQL) for writing and querying data.


**So SQLite ?**

    https://docs.python.org/3/library/sqlite3.html
    
    SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing 
    the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. 
    It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
 
 
# Connecting to database

**1_dbConnection.py**
    
This file has the code to connect to database.It includes

    import sqlite3
    connection = sqlite3.connect(database.db)
    cur = connection.cursor()
    
# Creating a table

**2_create.py**

CREATE query creates a table in the database.

    Syntax
    CREATE TABLE tablename (columnname1 datatype, columnname2 datatype, ...)
   
# Add data to a table

**3_insert.py**

INSERT query adds records to a table in the database.

    syntax
    INSERT INTO tablename VALUES(value1, value2, value3, ...)

# Read records form a table

**4_select.py**

SELECT query gets the records from a database table.

    syntax
    SELECT * FROM tablename

**4a_selectSomeCol.py**

SELECT some columns

    syntax
    SELECT columnname1, columnname2, ... FROM tablename

**5_selectwhere.py**

SELECT with WHERE clause
    
    syntax
    SELECT columnname1, columnname2, ... FROM tablename WHERE columname = value
   
 # Commit to a databse table
 
 **6_commit.py**
 
 This method commits the current transaction. If you don’t call this 
 method, anything you did since the last call to commit() is not visible 
 from other database connections. If you wonder why you don’t see the data 
 you’ve written to the database, please check you didn’t forget to call 
 this method.
 
    syntax
    connection.commit()
 
# Close a database

**7_close.py**

This closes the database connection. Note that this does not automatically call commit(). If you just close your database connection without calling commit() 
first, your changes will be lost!

    syntax 
    connection.close()
 
# Update records in a table

**8_update.py**

UPDATE query makes changes to the records already inserted in the table.

    syntax
    UPDATE tablename SET columnname= value WHERE condition

# Delete record from a table

**9_delete.py**

DELETE query removes the record from a table

    syntax
    DELETE FROM tablename WHERE condition

# Database file in SQLite

**10.database.db**

A database file will be generated in the current working directory. The file content will not be displayed in the editor because it is either binary or other.


