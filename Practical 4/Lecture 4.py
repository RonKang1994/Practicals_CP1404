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


def main():
    check_vowel()


main()