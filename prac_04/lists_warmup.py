"""This document contains warm up questions"""
numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] answer - 3
# numbers[-1] answer - 2
# numbers[3] answer - 1
# numbers[:-1] answer - [3, 1, 4, 1, 5, 9]
# numbers[3:4] - answer - [1]
# 5 in numbers - answer - True
# 7 in numbers - answer - False
# "3" in numbers - answer - False
# numbers + [6, 5, 3] - answer [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
if 9 in numbers:
    print("9 is in numbers")
else:
    print("9 is not in numbers")
