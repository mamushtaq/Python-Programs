import json

username = input("What is your username?\n")
filename = 'username.json'

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We will remember you next time")