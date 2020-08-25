import files
import sqlite3

Lusr_name = files.user_validation()

def text_store(file_name,file_ext,file_data):
    con = sqlite3.connect("userdatabase.db")
    c = con.cursor()
    c.execute('''INSERT INTO USERDATAS(FILENAME,FILEEXT,DATA) VALUES(?,?,?)''',(file_name,file_ext,file_data))
    con.commit()
    c.close()

def image_store(file_name,file_ext,file_data):
    con = sqlite3.connect("userdatabase.db")
    c = con.cursor()
    c.execute('''INSERT INTO USERDATAS(FILENAME,FILEEXT,DATA) VALUES(?,?,?)''',(file_name,file_ext,file_data))
    con.commit()
    c.close()



def open_stored_file(usr_ch,fname,fext):
    if usr_ch == int(1):
        con = sqlite3.connect("userdatabase.db")
        c = con.cursor()
        c.execute("SELECT DATA FROM USERDATAS WHERE FILENAME=?",(fname,))
        d = c.fetchone()
        for i in d:
            data = i
        datas = bytes(data,'utf-8')
        with open (fname+'.'+fext,"wb") as f:
            f.write(datas)
        return 1    
    elif usr_ch == int(2):
        con = sqlite3.connect("userdatabase.db")
        c = con.cursor()
        c.execute("SELECT DATA FROM USERDATAS WHERE FILENAME=?",(fname,))
        d = c.fetchone()
        imdata = d[0]
        with open(fname+'.'+fext,"wb") as d:
            d.write(imdata) 
        return 1
    else:
        print("invalid file extension")          
            


def store_file():
    con = sqlite3.connect("userdatabase.db")
    c = con.cursor()
    try:
        c.execute('''CREATE TABLE  USERDATAS(FILENAME VARCHAR(20),FILEEXT VARCHAR(5),DATA BLOB)''')
    except:
        print("PLEASE CHOOSE")
    print("\n")
    print("\n")

    print("What is the type of file you want to store")
    dic = {"TEXT = 1":".txt","IMAGE = 2":".img",}
    for i in dic:
        print(i)
    usr_ch = int(input("Enter your choice"))
    if usr_ch == int(1):
        file_name =  input("Enter your file name  ")
        file_ext = input("Enter the file extension")
        with open(file_name+"."+file_ext,"r") as f:
            file_data = f.read()
        text_store(file_name,file_ext,file_data)
    elif usr_ch == int(2):
        fname = input("Enter your file name  ")
        fext = input("Enter your file ext  ")
        with open(fname+"."+fext,"rb") as f:
            data = f.read()
        image_store(fname,fext,data)
    else:
        print("UNAVAILABE OPTION--CONTACT ADMIN")
        exit()

def open_file():
    fname = input("enter the name of the file  ")
    fext = str(input("Enter the extension of the file  "))
    if fext == 'txt':
        usr_ch = int(1)
        D = open_stored_file(usr_ch,fname,fext)
    else:
        usr_ch = 2
        D = open_stored_file(usr_ch,fname,fext)



    if D == int(1):
        print("YOUR FILE IS SUCESSFULLY RESTORED")
    else:
        print("FILE RESTORATION FAILED")

def show_files():
    con = sqlite3.connect("userdatabase.db")
    c = con.cursor()
    c.execute("SELECT FILENAME FROM USERDATAS")
    data = c.fetchall()
    print("These are your current file's stored in PROSAFE")
    for i in data:
        print(i[0])
    print("\n")
    c.close()

t = 1
while(t):
    print("#"*5 + " WELCOME TO PROSAFE " + "#"*5)
    print("\n")
    print("Choose your option: ")
    print("1.STORE FILE")
    print("2.OPEN FILE")
    print("3.SHOW FILES")
    print("4.QUIT PROSAFE")
    print("\n")
    i = int(input(">> "))
        
    if i == 1:
        store_file()
    elif i == 2:
        open_file()
    elif i == 3:
        show_files()
    else:
        exit()

        