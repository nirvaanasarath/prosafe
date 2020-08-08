import sqlite3

dbname = input("Enter your DB name ")
table_name = input("Enetr your table name ")
connection = sqlite3.connect("dbname")  #connecting to the specified DB
c = connection.cursor() #cursor() obj is used to execute SQLITE3 statement's 
c.execute('''CREATE TABLE table1(col1 int PRIMARY KEY,col2 char NOT NULL);''') #creates table
r = c.execute("SELECT name FROM sqlite_master where type = 'table'") #select all names of tables that exist's in the current DB
tables = r.fetchall() #fetcheall returns all outpun from the above stmnt.
for i in tables:
    print(i) #prints all o/p