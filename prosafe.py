def store_file():
    print("file stored")


def open_file():
    print("file opened")

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
    print("wrong")