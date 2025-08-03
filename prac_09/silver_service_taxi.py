"""Generate SilverServiceTaxi class"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Generate SilverServiceTaxi class"""
    flagfall = 4.5

    def __init__(self, fanciness, **kwargs):
        """Initialise a UnreliableCar instance."""
        super().__init__(**kwargs)
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the taxi trip."""
        return f"{super().__str__()} plus flagfall of {self.flagfall}"
