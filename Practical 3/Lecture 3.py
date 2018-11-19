import string


def count_letters(string_check):
    """Counts the number of letters in a sting"""
    count = 0
    for char in string_check:
        if char.lower() in string.ascii_lowercase:
            count+=1

    return count


def main():
    check_string = str("Hello World")
    num = count_letters(check_string)
    print("Number of letters: ", num)


main()