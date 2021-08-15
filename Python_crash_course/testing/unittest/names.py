from name_function import get_formatted_name

print("Please enter your name.\nEnter 'q' to quit.")

while True:
    firstname = input("Enter your first name: ")
    if firstname == 'q':
        break
    lastname = input("Enter your last name: ")
    if lastname == 'q':
        break
    fullname = get_formatted_name(firstname, lastname)
    print (f"Your formatted name is {fullname}\n")