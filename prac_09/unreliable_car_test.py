"""Test unreliable_car Class"""
from unreliable_car import UnreliableCar

c1 = UnreliableCar("Car1", 1000000, 30.0)
c2 = UnreliableCar("Car2", 1000, 30.0)
c1.drive(100)

n1 = 0
n2 = 0
for i in range(1000):
    x = c1.drive(100)
    print(f"Car 1: {x}")
    if x != 0:
        n1 += 1
    y = c2.drive(100)
    print(f"Car 2: {y}")
    if y != 0:
        n2 += 1
print(f"Car 1 traveled {n1} times")
print(f"Car 1 traveled {n2} times")
