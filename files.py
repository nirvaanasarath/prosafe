def create_new():
    print("new acnt created")


ch = input("Are you an existing user \n If yes = 1 If no = 0 > ")

if ch == 1:
    usr_name = input("Enter your user name ")
    psswd = input("Enter your password ")
else:
    new = int(input("Would you like to create a new PROSAFE account \n IF YES - 1 IF NO (QUIT) - 2 "))
    if new == 1:
        create_new()
    else:
        print("quit")

