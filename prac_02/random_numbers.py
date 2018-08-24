import random


def main():
    # line 1 (produced a random number between 5 and 20.
    # The smallest number is 5 and the largest is 20
    print(random.randint(5, 20))

    # It was producing a random number between 3 to 10 going in steps of 2.
    # The smallest number is 3 and the largest was 9
    print(random.randrange(3, 10, 2))

    # It was producing a random number between 2.5 and 5.5 with 16th decimal places
    # the smallest number is 2.5 and the largest is 5.5
    print(random.uniform(2.5, 5.5))


main()
