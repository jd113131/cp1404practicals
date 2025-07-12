"""Test the guitar class"""

from prac_06.guitar import Guitar

GuitarOne = Guitar("Guitar One", 1925, 1000)
GuitarTwo = Guitar("Guitar Two", 2001, 100)
GuitarThree = Guitar("Guitar Three", 1975, 300)

print(GuitarOne)
print(GuitarTwo)
print(GuitarThree)

print(f"Guitar One get_age() - Expected 100. Got {GuitarOne.get_age()}")
print(f"Guitar Two get_age() - Expected 24. Got {GuitarTwo.get_age()}")
print(f"Guitar Three get_age() - Expected 50. Got {GuitarThree.get_age()}")

print(f"Guitar One is_vintage() - Expected True. Got {GuitarOne.is_vintage()}")
print(f"Guitar Two is_vintage() - Expected Fase. Got {GuitarTwo.is_vintage()}")
print(f"Guitar Three is_vintage() - Expected True. Got {GuitarThree.is_vintage()}")
