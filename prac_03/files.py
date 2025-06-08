"""Practice reading and righting to files"""

FILE_NAME = "name.txt"
FILE_NUMBERS = "numbers.txt"
# 1
name = input("what is your name? ")
in_file = open(FILE_NAME, 'w')
print(name, file = in_file)
in_file.close()

# 2
try:
    out_file = open(FILE_NAME, 'r')
    name = out_file.read()
    print(f"Hi {name.strip()}!")
    out_file.close()
except FileNotFoundError:
    print("File not found")

#3
try:
    with open(FILE_NUMBERS, 'r') as in_file:
        number = int(in_file.readline().strip())
        number += int(in_file.readline().strip())
        print(number)
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Could not convert to an integer.")
    in_file.close()

# 4
try:
    with open(FILE_NUMBERS, 'r') as in_file:
        number = 0
        for line in in_file.readlines():
            number += int(line.strip())
        print(number)
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Could not convert to an integer.")
    in_file.close()

