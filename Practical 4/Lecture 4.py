def main():
    name = str(input("Name: "))
    letters = 0
    vowels = 0
    for char in name:
        letters+=1
        if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
            vowels+=1

    print("Out of {} letters {} has {} vowels".format(letters, name, vowels))


main()