def grad_string(score):
    if score < 0 or score > 100:
        grade = "Invalid score"
    elif score > 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"

    return grade


def main():
    score = float(input("Enter score: "))
    grade = grad_string(score)
    print(grade)


main()