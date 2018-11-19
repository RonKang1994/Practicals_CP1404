def read_from_file():
    names = open('name.txt', 'r')

    name_output = names.read()
    print(name_output)

    names.close()


def write_in_file():
    names = open('name.txt', 'w')

    name_input = str(input("May i have your name: "))
    print("Your name is", name_input, file=names)

    names.close()


def read_n_add():
    number_file = open('numbers.txt', 'r')

    # num1 = int(number_file.readline())
    # num2 = int(number_file.readline())
    # sum = num1 + num2
    sum = 0
    for line in number_file:
        number = int(line)
        sum += number

    print("The sum is: ", sum)

    number_file.close()


def main():

    # write_in_file()
    #
    # read_from_file()

    read_n_add()


main()