"""Generate unreliable car subclass."""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Unreliable car class."""
    def __init__(self, name, fuel, reliability: float):
        """Initialise a UnreliableCar instance."""
        # Car.__init__(self, name, fuel)
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on distance if passes reliability."""
        if randint(0, 100) < self.reliability:
            return Car.drive(self, distance)
        else:
            return 0