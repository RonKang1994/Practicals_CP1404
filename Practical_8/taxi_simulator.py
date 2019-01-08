from Practical_8.taxi import Taxi
from Practical_8.silver_taxi import SilverServiceTaxi


def menu():
    print("q)uit, c)hoose taxi, d)rive")


def show_taxis(taxis, choice_menu):
    if choice_menu != "q":
        print("Taxis available:")
        for i in range(len(taxis)):
            print(i, " - ", taxis[i])
    else:
        print("Taxis are now:")
        for i in range(len(taxis)):
            print(i, " - ", taxis[i])


def current_bill(trip_cost):
    print("Bill to date: ${:.2f}".format(trip_cost))


def main():
    """Cost of total trip"""
    trip_cost = 0
    """Used to check for user choice in the main menu"""
    choice_menu = ''
    """Used to check which taxi the user wants"""
    choice_taxi = int(-1)
    """Distance the user wants to drive"""
    drive_dist = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    while choice_menu.lower() != 'q':
        menu()
        choice_menu = input(">>> ")
        if choice_menu.lower() != "c" and choice_menu.lower() != "d" and choice_menu.lower() != "q":
            print("Invalid Input")
        elif choice_menu.lower() == 'c':
            show_taxis(taxis, choice_menu)
            choice_taxi = int(input("Choose Taxi: "))
            while choice_taxi < 0 or choice_taxi >= int(len(taxis)):
                print("Invalid Choice")
                choice_taxi = int(input("Choose Taxi: "))
            current_bill(trip_cost)
        elif choice_menu.lower() == 'd':
            if choice_taxi < 0:
                """Error check to ensure a taxi must be chosen first"""
                print("Taxi has not yet been chosen")
            else:
                drive_dist = int(input("Drive how far?"))
                while drive_dist < 0:
                    print("Invalid Choice")
                    drive_dist = int(input("Drive how far?"))
                taxis[choice_taxi].start_fare()
                taxis[choice_taxi].drive(drive_dist)
                print("Your {} trip cost you ${:.2f}".format(taxis[choice_taxi].name, taxis[choice_taxi].get_fare()))
                trip_cost = trip_cost + taxis[choice_taxi].get_fare()
            current_bill(trip_cost)
            # print("Do d Stuff")
        else:
            print("Do Stuff")

    if choice_menu.lower() == 'q':
        print("Total trip cost: ${:.2f}".format(trip_cost))
        show_taxis(taxis, choice_menu)


main()