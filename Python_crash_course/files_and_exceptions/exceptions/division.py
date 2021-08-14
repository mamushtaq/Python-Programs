print("I will divide two numbers for you.\nEnter 'q' to quit")
while True:
    first_number = input("\nEnter first number : ")
    if first_number == 'q':
        break
    second_number = input("\nEnter second number : ")
    if second_number == 'q':
        break
    try:
        print(int(first_number)/int(second_number))
    except ZeroDivisionError:
        print("\nCannot be divided by zero")