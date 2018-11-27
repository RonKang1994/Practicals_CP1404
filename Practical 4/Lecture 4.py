VOWELS_CHECK = 'aeiou'


def check_vowel():
    name = str(input("Name: "))
    letter = 0
    vowel = 0
    for char in name:
        letter += 1
        for v_check in VOWELS_CHECK:
            if char.lower() == v_check.lower():
                vowel += 1
    print("Out of {} letters {} has {} vowels".format(letter, name, vowel))


def long_list(text):
    text_list = text.split()
    final_list = list()
    for i in range(0, len(text_list)):
        if len(text_list[i]) > 3:
            final_list.append(text_list[i])
    print(final_list)


def main():
    # Give a name and check how many vowels there are in it
    # check_vowel()

    # Convert a string into a list and give ones which have 3> characters
    text = "This is a sentence"
    long_list(text)


main()