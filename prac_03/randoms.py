"""Testing random functions"""

# What did you see on line 1?
# 17, 12, 16, 11, 16, 20

# What was the smallest number you could have seen, what was the largest?
# smallest is 5, largest is 20


# What did you see on line 2?
# 5, 9, 3, 9, 7, 3

# What was the smallest number you could have seen, what was the largest?
# smallest number that could have been seen was 3, largest nuber that could have been seen was 9

# Could line 2 have produced a 4?
# No as it starts with a odd number and increments by 2


# What did you see on line 3?
# 3.7101094441920828, 4.433023246483669, 5.041771111196591, 4.26252827334774, 4.932238949715874, 4.80524791671184

# What was the smallest number you could have seen, what was the largest?
# the smallest value that could have been seen is 2.5 and, the largest value in this cases is 5.5 as it is a float value
# however if it was not a float value it would have been the next closes smaller float value

import random

def main():
    """Produces a random number" between 1 and 100"""
    for i in range(100):
        random_number = random.randint(1, 100)
        print(random_number)

main()
