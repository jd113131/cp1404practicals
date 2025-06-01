
x = int(input("Enter x: "))
y = int(input("Enter y: "))

if (x % 2) == 1:
    x_is_odd = 1
else:
    x_is_odd = 0

print("Type (1) to show the even numbers from x to y")
print("Type (2) to show the odd numbers from x to y")
print("Type (3) to show the squares of the numbers from x to y")
print("Type (4) to exit the program")
choice = input(">>> ")

while choice != '4':

    if choice == '1':
        for i in range(x + x_is_odd, y + 1,2):
            print(f"{i}", end=" ")
        print()
    elif choice == '2':
        for i in range(x + (1 ^ x_is_odd), y + 1 ,2):
            print(f"{i}", end=" ")
        print()
    elif choice == '3':
        for i in range(x, y + 1):
            print(f"{i**2}", end=" ")
        print()
    else:
        print("Invalid choice")

    print("Type (1) to show the even numbers from x to y")
    print("Type (2) to show the odd numbers from x to y")
    print("Type (3) to show the squares of the numbers from x to y")
    print("Type (4) to exit the program")
    choice = input(">>> ")


print("program terminated")
