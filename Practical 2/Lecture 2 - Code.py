def age_average():
    age = 0
    count = 0
    total_age = 0
    while age >= 0:
        age = int(input("Input age: "))
        if age >= 0:
            count += 1
            total_age += age
        else:
            average = int(total_age / count)

    print("Average age: ", average)



def money_printer():
    name = str(input("Name: "))
    money = float(input("Money: "))
    print("{} has ${:.2f}".format(name, money))



def main():
    # age_average()
    money_printer()




main()