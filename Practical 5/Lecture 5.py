def highest_age(names, ages):
    name = ""
    age = 0
    # for i in range(len(names)):
    #     if age < ages[i]:
    #         age = ages[i]
    #         name = names[i]
    #
    # return name
    name = names[ages.index(max(ages))]
    return name


def add_dict():
    ages_dict = {"Bill": 21, "Jane": 4, "Jack": 56}
    # name = str(input("Name: "))
    # age = int(input("Age: "))
    # for i in range(len(ages_dict)):
    #     print(ages_dict[i])


def main():
    # names = ["Jim", "Mary", "Tim"]
    # ages = [10, 50, 20]
    # name = highest_age(names, ages)
    # print("The oldest person is {}".format(name))
    add_dict()


main()