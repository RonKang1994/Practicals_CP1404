def checkAge(age):
    if (age >= 1 and age <= 150):
        return True
    else:
        print("Invalid Age")
        return False

def muliTwo(num):
    numResult = num * 2
    return numResult

def adult_child(age):
    if (age < 18):
        print("You are a child")
    else:
        print("You are an adult")

def main():
    # age = int(input("Can i have your age: "))
    #
    # while(checkAge(age) == False):
    #     age = int(input("Can i have your age: "))
    #
    # print("Your age is: ", age)

    # num1 = int(input("Can i have a number: "))
    #
    # print("Your number", num1,"* 2 is: ", muliTwo(num1))

    age = int(input("Can i have your age: "))

    while(checkAge(age) == False):
        age = int(input("Can i have your age: "))

    print("Your age is: ", age)
    adult_child(age)

main()