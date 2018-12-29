from Practical_8.silver_taxi import SilverServiceTaxi


def main():
    fancy_taxi = SilverServiceTaxi("Royal", 100, 2)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print(fancy_taxi.get_fare())

main()