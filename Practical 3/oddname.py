def skip_numbers():
    num = int(input("Skip number - "))
    while num <= 0:
        print("Invalid input enter again")
        num = int(input("Skip number - "))

    return num


def get_name():
    name = input("Enter name - ")
    """Check that name is not blank"""
    while len(name) <= 0:
        print("Name is blank enter again.")
        name = input("Enter name - ")
    return name


def print_name(name, num):
    """Print odd characters in the name version 1"""
    # print(name[::num])
    """Print odd characters in the name version 2"""
    for i in range(0, len(name), num):
        print(name[i], end='')


def main():
    """Input name and print odd characters"""
    name = get_name()

    num = skip_numbers()

    print_name(name, num)


main()