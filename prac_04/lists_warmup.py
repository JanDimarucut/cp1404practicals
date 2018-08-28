"""

numbers [0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = 3,1,4,1,5,9
numbers[3:4] = 1,5
5 in numbers = True
7 in numbers = False
"3" in numbers = invalid (it's a string)
numbers + [6, 5, 3] = 3,1,4,1,5,9,2,6,5,3

"""

number = [3, 1, 4, 1, 5, 9, 2]

# 1
number[0] = 10

# 2
number[-1] = 1

# 3
print(number[2:])

# 4
if 9 in number:
    print(True)
else:
    print(False)
