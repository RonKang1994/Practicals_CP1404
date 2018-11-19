TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def temp_convert():
    """
    CP1404/CP5632 - Practical
    Pseudocode for temperature conversion
    """

    MENU = """    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
            # pass
            fahrenheit = float(input("Fahrenheit: "))
            celsius = 5 / 9 * (fahrenheit - 32)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def sales_bonus():
    """
    Program to calculate and display a user's bonus based on sales.
    If sales are under $1,000, the user gets a 10% bonus.
    If sales are $1,000 or over, the bonus is 15%.
    """
    sales = float(input("Sales Amount:$ "))
    if sales < 0:
        print("Invalid Amount")
    elif sales < 1000:
        bonus = sales / 100 * 10
        print("Bonus:$ {:.2f}".format(bonus))
    else:
        bonus = sales / 100 * 15
        print("Bonus:$ {:.2f}".format(bonus))


def grades():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def loops():
    for i in range(1, 21, 2):
        print(i, end=' ')

    print("\n")

    for i in range(0, 101, 10):
        print(i, end=' ')

    print("\n")

    for i in range(20, 0, -1):
        print(i, end=' ')
    # print()


def sales_bonus_loop():
    """
    Program to calculate and display a user's bonus based on sales.
    If sales are under $1,000, the user gets a 10% bonus.
    If sales are $1,000 or over, the bonus is 15%.
    """
    sales = 0
    while sales >= 0:
        sales = float(input("Sales Amount:$ "))
        if sales < 0:
            print("Invalid Amount")
        elif sales < 1000:
            bonus = sales / 100 * 10
            print("Bonus:$ {:.2f}".format(bonus))
        else:
            bonus = sales / 100 * 15
            print("Bonus:$ {:.2f}".format(bonus))


def shop_calculator():
    items = int(input("Number of items: "))
    while items < 0:
        print("Invalid number of items!")
        items = int(input("Number of items: "))

    prices = [0] * items
    total_price = 0
    for i in range(0, items, 1):
        prices[i] = float(input("Price of item: "))
        while prices[i] < 0:
            print("Invalid price!")
            prices[i] = float(input("Price of item: "))

        total_price += prices[i]

    if total_price >= 100:
        # total_price = total_price / 10 * 9
        total_price *= 0.9
        print("Total price for", items, "item(s) is ${:.2f}".format(total_price))
    else:
        print("Total price for", items, "item(s) is ${:.2f}".format(total_price))


def electric_bill():
    print("Electricity bill estimator\n")
    bill = float(input("Enter cents per kWh: "))
    electricity = float(input("Enter daily use in kWh: "))
    total_days = float(input("Enter number of billing days: "))
    estimate_bill = (bill * electricity * total_days) / 100

    print("Estimated bill: $ {:.2f}".format(estimate_bill))


def electric_bill_2():
    print("Electricity bill estimator 2\n")
    tarif_choice = float(input("Which tariff? 11 or 31: "))
    if tarif_choice == 11:
        tarif_selection = TARIFF_11
    elif tarif_choice == 31:
        tarif_selection = TARIFF_31

    electricity = float(input("Enter daily use in kWh: "))
    total_days = float(input("Enter number of billing days: "))
    estimate_bill = (tarif_selection * electricity * total_days)

    print("Estimated bill: $ {:.2f}".format(estimate_bill))


def main():
    # print("Hello World")
    # Part 1
    temp_convert()

    # Part 2
    # sales_bonus()

    # Part 3
    # grades()

    # Part 4
    # loops()

    # Part 5
    # sales_bonus_loop()

    # Part 6
    # shop_calculator()

    # Part 7
    #electric_bill()

    # Part 8
    # electric_bill_2()


main()
