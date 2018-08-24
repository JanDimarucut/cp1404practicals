# 1) Asks for the user's name
out_file = open("name.txt", 'w')
user_name = input("Enter your name: ")
print(user_name, file=out_file)
out_file.close()

# 2) Opens the name.txt and prints the name
in_file = open("name.txt", 'r')
user_name = in_file.read().strip()
print("Your name is {}".format(user_name))
in_file.close()

# 3) Opens the numbers.txt and prints out the total number
in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
number1 += number2
print(number1)
in_file.close()
