TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

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
    # Part 7
    electric_bill()

    # Part 8
    # electric_bill_2()


main()