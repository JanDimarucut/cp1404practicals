# 4

def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    add_memberwise(list1, list2)


def add_memberwise(list1, list2):
    list3 = [(x + y) for x, y in zip(list1, list2)]
    print(list3)


main()
