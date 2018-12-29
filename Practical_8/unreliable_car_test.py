from Practical_8.unreliable_car import UnreliableCar


def main():
    old_reliable = UnreliableCar("Jankins", 100, 50)
    old_reliable.drive(10)
    print(old_reliable)

main()