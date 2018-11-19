def main():
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


main()