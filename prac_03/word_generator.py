import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    word_format = input(">")
    word = ""
    format_word = is_valid_format(word_format, word)
    print(format_word)


def is_valid_format(word_format, word):
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
            return True

        elif kind == "v":
            word += random.choice(VOWELS)
            return True

        else:
            return False


main()
