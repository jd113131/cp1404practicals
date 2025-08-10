"""Test silver service taxi class"""

from silver_service_taxi import SilverServiceTaxi

silver_service_taxi = SilverServiceTaxi("Hummer", 500, 2)
print(silver_service_taxi)
silver_service_taxi.drive(18)
print(silver_service_taxi.get_fare())
silver_service_taxi.start_fare()
print(silver_service_taxi.get_fare())