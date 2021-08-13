with open("py_digits.txt") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

pi_digits = ""

for line in lines:
    pi_digits += line.strip()

print(pi_digits)
print(len(pi_digits))