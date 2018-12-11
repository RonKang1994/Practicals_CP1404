from prac_06.car import Car


def main():
    """Test code to used Car class"""
    my_car = Car(180, "car")
    my_car.drive(30)
    limo = Car(100, "Limo")
    limo.add_fuel(20)
    # print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print("limo fuel =", limo.fuel)
    limo.drive(115)
    print("limo odometer =", limo.odometer)
    print(limo)


main()