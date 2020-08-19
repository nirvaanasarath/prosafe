def user_validation():
    import sqlite3

    con = sqlite3.connect("userdatabase.db")
    c = con.cursor()
    try:
        c.execute('''CREATE TABLE USERINFO([generated_id] INTEGER PRIMARY KEY,NAME CHAR(20) NOT NULL,PASSWORD CHAR(20) NOT NULL)''')
    except sqlite3.Error as error:
        print("Table already exist's")
        

    def create_new():
        new_name = input("Enter your user name")
        new_psswd = input("Enter your passwd")
        c.execute('''INSERT INTO USERINFO(NAME,PASSWORD) VALUES(?,?)''',(new_name,new_psswd))
        con.commit()
        c.close()


    ch = int(input("Are you an existing user \n If yes = 1 If no = 0 > "))

    if ch == 1:
        usr_name = input("Enter your user name ")
        psswd = str(input("Enter your password "))
        con = sqlite3.connect("userdatabase.db")
        c = con.cursor()
        k = c.execute('''SELECT PASSWORD FROM USERINFO WHERE NAME=?''',(usr_name,))
        tupledata = k.fetchone() 
        c.close()
        try:
            for i in tupledata:
                key = i
        except:
            print("No such user exist's")
            print("PROSAFE TERMINATED")
            exit()

        if key == psswd:
            print("LOGIN SUCESS")
        else:
            print("LOGIN FAILED")
            exit()

    else:
        new = int(input("Would you like to create a new PROSAFE account \n IF YES - 1 IF NO (QUIT) - 2 "))
        if new == 1:
            create_new()
        else:
            print("quit")
            exit()

