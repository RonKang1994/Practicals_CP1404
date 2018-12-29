"""
Testing out my Taxi Class
"""
from Practical_8.taxi import Taxi


def main():
    """Initialise my Test Taxi"""
    test_taxi = Taxi("Prius 1", 100)

    """Drive my Test Taxi for 40km"""
    test_taxi.drive(40)

    """Print Fare Amount"""
    print(test_taxi, "/n Current Fare: ${:.2f}".format(test_taxi.get_fare()))

    """Rest Test Taxi fare"""
    test_taxi.start_fare()

    """Drive my Test Taxi for 100km and print fare again"""
    test_taxi.drive(100)
    print(test_taxi, "/n Current Fare: ${:.2f}".format(test_taxi.get_fare()))


main()