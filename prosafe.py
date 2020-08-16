import base64


org_pass = 123456

def store_file():
    type_file = input("What is the extension of the file you want to store today")
    



def open_file():
    print("file opened")

# pass = input("Enter your PASSWORD >> ")
print("enter pass")
p = int(input())

if p == org_pass:
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
else:
    print("wrong")