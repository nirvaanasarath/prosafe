import json

def create_new():
    # file = open("user_data.json","a")
    new_usr_name = input("Enter your name ")
    new_use_pswd = input("Enter your psswd ")
    my_dict = ({new_usr_name : new_use_pswd})
    j =  json.dumps([my_dict])
    with open("user_data.json","a") as f:
        f.write(j)
        f.close()

def usr_info(usr_name):
    data = json.load(open("user_data.json","r"))
    key = data.get(usr_name)
    return key



ch = int(input("Are you an existing user \n If yes = 1 If no = 0 > "))

if ch == 1:
    usr_name = input("Enter your user name ")
    psswd = input("Enter your password ")
    rkey = usr_info(usr_name)
    
    if rkey == psswd:
        print("LOG IN SUCESS")
    else:
        print("LOGIN FAILED")

else:
    new = int(input("Would you like to create a new PROSAFE account \n IF YES - 1 IF NO (QUIT) - 2 "))
    if new == 1:
        create_new()
    else:
        print("quit")
        

