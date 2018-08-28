LOWER = 33
UPPER = 127


def main():
    """Get and convert ASCII values/characters."""
    char = input("Enter a letter: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))
    number = get_number_between(LOWER, UPPER)
    print("The character for {} is {}".format(number, chr(number)))

    # ASCII table (no columns)
    for value in range(LOWER, UPPER + 1):
        print("{:3} {:>4}".format(value, chr(value)))


def get_number_between(LOWER, UPPER):
    """Get a valid number between the given parameters."""
    number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
    while number < LOWER or number > UPPER:
        number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
    return number


main()
