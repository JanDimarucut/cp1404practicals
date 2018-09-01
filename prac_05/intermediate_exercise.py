COLOUR_CODE = {"Blue": "#0000ff", "Red": "#ff0000", "Yellow": "#ffff00", "Orange": "#ffa500", "Green": "#00ff00",
               "Pink": "#ffc0cb", "Black": "#000000", "Brown": "#a52a2a", "Gold": "#ffd700", "Purple": "#a020f0"}

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    if colour_name in COLOUR_CODE:
        print(colour_name, "is", COLOUR_CODE[colour_name])
    else:
        print("Invalid input")
    colour_name = input("Enter colour name: ").title()