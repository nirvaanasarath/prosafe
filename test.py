import sqlite3

dbname = ("Enter your DB name ")
connection = sqlite3.connect("dbname")
c = connection.cursor()
# c.execute('''CREATE TABLE table1(col1 int PRIMARY KEY,col2 char NOT NULL);''')
r = c.execute("SELECT name FROM sqlite_master where type = 'table'")
tables = r.fetchall()
for i in tables:
    print(i)