"""
Loops
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
number_of_stars = int(input("Nmber of stars: "))
while number_of_stars < 0:
    print("Invalid number")
    number_of_stars = int(input("Nmber of stars: "))

for i in range(0, number_of_stars, 1):
    print('*', end='')
print()

# d

for i in range(0, number_of_stars, 1):
    for j in range(0, i+1, 1):
        print('*', end='')
    print()
print()