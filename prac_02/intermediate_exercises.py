finished = False
result = 0
while not finished:
    try:
        # TODO: this line
        # TODO: this line
        pass
    except:  # TODO - add something after except
        print("Please enter a valid integer")
print("Valid result is:", result)

# The finished version by adding all necessary codes
finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a number: "))
        finished = True
    except ValueError:
        print("Please enter a number.")
print("Valid result is: {}".format(result))
