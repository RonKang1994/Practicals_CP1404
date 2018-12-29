"""
CP1404/CP5632 Practical
Car class
"""
from Practical_8.car import Car
import random

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(fuel, name)
        self.reliability = reliability

    def __str__(self):
        return "{}".format(super().__str__())

    def drive(self, distance):
        check = random.randrange(0, 100)
        print(check)
        distance_driven = 0
        if check < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven