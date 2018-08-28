MINIMUM_LENGTH = 2


def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password, ensuring it meets the minimum_length requirement."""
    password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter password of at least {} characters: ".format(minimum_length))
    return password


def print_asterisks(password):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    get_password(password)


def get_password(password):
    print('*' * len(password))


def get_password():
    main()


get_password()
