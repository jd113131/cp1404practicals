"""Testing code fro taxi class"""
from prac_09.taxi import Taxi

# 1
my_taxi = Taxi("Prius 1", 100, 1.23)
# 2
my_taxi.drive(40)
# 3
print(f"{my_taxi} the current fare is {my_taxi.get_fare()}")
# 4
my_taxi.start_fare()
my_taxi.drive(100)
# 5
print(f"{my_taxi} the current fare is {my_taxi.get_fare()}")