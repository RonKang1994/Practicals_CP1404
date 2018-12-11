from prac_06.guitar import Guitar


def main():
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    new_guitar = Guitar("Another guitar", 2012, 1035.40)
    print(my_guitar)
    print("Vintage: {}".format(str(my_guitar.is_vintage())))
    print("Year old: {}".format(my_guitar.get_age()))
    print(new_guitar)
    print("Vintage: {}".format(str(new_guitar.is_vintage())))
    print("Year old: {}".format(new_guitar.get_age()))


main()
