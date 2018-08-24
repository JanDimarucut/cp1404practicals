MIN_LENGTH = 2
MAX_LENGTH = 6


def main():
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and "
          "contains".format(MIN_LENGTH, MAX_LENGTH))
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")

    password = input(">")

    while not is_valid_password(password):
        print("Invalid Password")
        password = input(">")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_digit = 0
    count_upper = 0
    count_lower = 0

    for character in password:
        if character.isupper():
            count_upper += 1

        elif character.islower():
            count_lower += 1

        elif character.isdigit():
            count_digit += 1

    if count_digit == 0 or count_lower == 0 or count_upper == 0:
        return False

    else:
        return True


main()
