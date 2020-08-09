import json

# global my_dict = {}
def create_new():
    file = open("user_data.json","a")
    new_usr_name = input("Enter your name ")
    new_use_pswd = input("Enter your psswd ")
    my_dict = ({new_usr_name : new_use_pswd})
    json.dump(my_dict,file)
    file.close()

# def view_users():
#     file =  open("user_data.json","r")
#     print(my_dict.keys())
#     file.close()


ch = input("Are you an existing user \n If yes = 1 If no = 0 > ")

if ch == 1:
    usr_name = input("Enter your user name ")
    psswd = input("Enter your password  ")
else:
    new = int(input("Would you like to create a new PROSAFE account \n IF YES - 1 IF NO (QUIT) - 2 "))
    if new == 1:
        create_new()
    else:
        print("quit")
        # view_users()

