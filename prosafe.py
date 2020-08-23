import files
import sqlite3

Lusr_name = files.user_validation()

def text_store(file_name,file_ext,file_data):
    con = sqlite3.connect("userdatabase.db")
    c = con.cursor()
    c.execute('''INSERT INTO USERDATAS(FILENAME,FILEEXT,DATA) VALUES(?,?,?)''',(file_name,file_ext,file_data))
    con.commit()
    c.close()

def open_stored_file():
    con = sqlite3.connect("userdatabase.db")
    c = con.cursor()
    c.execute('''SELECT TEXTDATA FROM USERINFO WHERE ''')


def store_file():
    con = sqlite3.connect("userdatabase.db")
    c = con.cursor()
    # c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ", (Lusr_name,))
    # tb = c.fetchone()
    # if tb == None: 
        # pass
    # else:
        # print("table does not exist") 
    try:
        c.execute('''CREATE TABLE USERDATAS(FILENAME VARCHAR(20),FILEEXT VARCHAR(5),DATA BLOB)''')
    finally:
        print("TABLE EXISTS")
    print("What is the type of file you want to store")
    dic = {"TEXT = 1":".txt","IMAGE = 2":".img",}
    for i in dic:
        print(i)
    usr_ch = int(input("Enter your choice"))
    if usr_ch == int(1):
        text_path = input("Drop your file here")
        file_name =  input("Enter your file name")
        file_ext = input("Enter the file extension")
        with open(file_name+"."+file_ext,"r") as f:
            file_data = f.read()
        text_store(file_name,file_ext,file_data)
    elif usr_ch == int(2):
        image_store()
    else:
        print("UNAVAILABE OPTION--CONTACT ADMIN")
        exit()

  
def open_file():
    print("file opened")




t = 1
while(t):
    print("#"*5 + " WELCOME TO PROSAFE " + "#"*5)
    print("\n")
    print("Choose your option: ")
    print("1.STORE FILE")
    print("2.OPEN FILE")
    print("3.QUIT PROSAFE")
    print("\n")
    i = int(input(">> "))
        
    if i == 1:
        store_file()
    elif i == 2:
        open_file()
    else:
        break
