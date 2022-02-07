# pip install mysql-connector-python

import mysql.connector

# connecting to mysql database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="pythontest"
)

print(mydb)

cursor = mydb.cursor()

# displaying table data before updating 
cursor.execute('SELECT * FROM Student')
for i in cursor:
    print(i)

# Updating marks of student
cursor.execute("UPDATE Student SET mark = 96 WHERE rollno = 2")

# displaying table data after updating
cursor.execute('SELECT * FROM Student')
print()
for i in cursor:
    print(i)

# saving the changes to database
mydb.commit()

# closing connections
cursor.close()
mydb.close()

