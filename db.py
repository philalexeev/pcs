import sqlite3

# create database while the program is running
# connection = sqlite3.connect(":memory:")

# connect or create database
# type(connection) === <class 'sqlite3.Connection'>
connection = sqlite3.connect("db/test_database.db")

# create cursor object to store and retrive data
# type(cursor) === <class 'sqlite3.Cursor'>
cursor = connection.cursor()

query = "SELECT datetime('now', 'localtime');"
results = cursor.execute(query)
print(results)

row = results.fetchone()
print(row)

time = row[0]
print(time)

connection.close()

