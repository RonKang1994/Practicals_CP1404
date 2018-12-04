def main():
    """
    CP1404/CP5632 Practical
    Color names in a dictionary
    """
    COLOR_NAMES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine": "#7fffd4",
                   "azure": "#f0ffff", "beige": "#f5f5dc", "bisque": "#ffe4c4", "black": "#000000",
                   "blueviolet": "#8a2be2", "brown	": "#a52a2a", "chocolate": "#d2691e"}

    color = input("Enter color: ")
    while color != "":
        if color.lower() in COLOR_NAMES:
            print(color.lower(), "color code is", COLOR_NAMES[color.lower()])
        elif color.upper() == "ALL":
            for color in COLOR_NAMES:
                print(color, "color code is", COLOR_NAMES[color])
        else:
            print("Invalid short state")
        color = input("Enter color: ")

main()