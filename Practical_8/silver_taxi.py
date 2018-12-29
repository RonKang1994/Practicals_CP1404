from Practical_8.taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness
        self.flagfall = 4.50

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        fare = self.price_per_km * self.current_fare_distance + self.flagfall
        """Round fare to the nearest 10cents"""
        fare = round(fare, 1)
        return fare