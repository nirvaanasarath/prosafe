import base64

# data = "sarath"
# encoded = base64.b64encode(data.encode("utf-8"))
# print(encoded)
# decoded = base64.b64decode(encoded)
# print(decoded)
# print(type(decoded))
# print(type(encoded))

# import pickle
import json
file = open("user_date.json","a")
new_usr_name = input("Enter your name ")
new_use_pswd = input("Enter your psswd")
my_dict = ({new_usr_name : new_use_pswd})
json.dump(my_dict,file)
file.close()
# f = open("usr_date.txt","r")

# file = open("user_date.json","r")
# print(my_dict.get(new_usr_name))
# print(my_dict.keys())