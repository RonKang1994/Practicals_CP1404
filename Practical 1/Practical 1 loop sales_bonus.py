def main():
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


main()