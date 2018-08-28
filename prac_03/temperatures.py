MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = converting_Celsius_to_Fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = converting_Fahrenheit_to_Celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


# converting to Celsius to Fahrenheit
def converting_Celsius_to_Fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


# converting to Fahrenheit to Celsius
def converting_Fahrenheit_to_Celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
