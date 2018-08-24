import random


quick_pick_number = int(input("How many quick picks? "))

for i in range(quick_pick_number):
    quick_pick = []
    for j in range(6):
        numbers = random.randint(1, 45)
        quick_pick.append(numbers)
    quick_pick.sort()
    print(" ".join("{:2}".format(numbers) for numbers in quick_pick))