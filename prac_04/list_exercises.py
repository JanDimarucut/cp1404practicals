# 1
numbers = []

for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

# print("The first number is: ", numbers[0])
# print("The last number is: ", numbers[-1])
# print("The smallest number is: ", min(numbers))
# print("The largest number is: ", max(numbers))
# print("The average of the numbers is: ", sum(numbers) / len(numbers))

# 2
user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
              'BaseStdIn', 'Command', 'ExerState', 'InteractiveConsole', 'InterpreterInterface',
              'StartServer', 'bob']

user_input = input("Please enter your username")
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")

# 3
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in
                 full_names]
print(full_initials)

# one more example, using filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# use a list comprehension to create a list of all of the full_names
# Names printed in all capital letters
capital_names = []
all_full_names = [name.upper() for name in full_names]
capital_names.append(all_full_names)
print(capital_names)

# in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# use a list comprehension to create a list of integers
# Numbers sorted from smallest to biggest
sorted_int = []
almost_numbers.sort()
sorted_int += almost_numbers
print(sorted_int)

# from the above list of strings
numbers = [int(almost_number) for almost_number in almost_numbers]
print(numbers)

# use a list comprehension to create a list of only the numbers that are
over_nine = []
bigger_number = [number for number in numbers if number > 9]
over_nine.append(bigger_number)
print(over_nine)

# greater than 9 from the numbers (not strings) you just created
big_numbers = [number for number in numbers if number > 9]
print(big_numbers)


