with open("py_digits.txt") as file_object:
    lines = file_object.readlines()

pi_digits = ""

for line in lines:
    pi_digits += line.strip()

birthday = input("Enter your birthday in the format mmddyyyy: ")
if birthday in pi_digits:
    print("Your birthday is in the first 1000 digits of pi")
else:
    print("Your birthday is not in first 1000 pi_digits")
