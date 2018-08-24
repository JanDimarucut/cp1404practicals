# Answer the following questions:
# 1. When will a ValueError occur?
# When the user enters an invalid input such as string instead of an integer
# (a letter instead of at number)

# 2. When will a ZeroDivisionError occur?
# When user enters 0 for numerator and 0 for denominator

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# No


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 3 Alternative programming to remind user that it's a ZeroDivisionError
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

while numerator == 0 and denominator == 0:
    print("You can't divide 0 to numerator and denominator")
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

fractions = numerator / denominator
print(fractions)
