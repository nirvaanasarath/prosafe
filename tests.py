import sqlite3

con = sqlite3.connect("userdatabase.db")
c = con.cursor()
# c.execute('''SELECT DATA FROM main.USERDATAS WHERE FILENAME = "HAI" & FILEEXT="txt"''')
c.execute('''SELECT * FROM USERDATAS''')
d = c.fetchall()
print(type(d))
print(d)
