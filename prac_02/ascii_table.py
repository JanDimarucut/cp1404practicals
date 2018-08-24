LOWER = 33
UPPER = 127

char = input("Enter a letter: ")
print("The ASCII code for {} is {}".format(char, ord(char)))
number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
print("The character for {} is {}".format(number, chr(number)))

# ASCII table (no columns)
for value in range(LOWER, UPPER + 1):
    print("{:3} {:>4}".format(value, chr(value)))