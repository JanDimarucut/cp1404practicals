NAMES = {"Bill": "", "Jane": "", "Ben": "", "Jack": "", "Jill": ""}

for name in NAMES:
    print("{}'s date of birth".format(name))
    user_input = input(">>>")
    NAMES[name] = user_input
print(NAMES)


# 2
def main():
    names = []
    dob = []
    for i in range(3):
        user_name = input("Enter name: ")
        names.append(user_name)

        user_dob = input("Enter D.O.B: ")
        dob.append(user_dob)
    get_user_input(names, dob)


def get_user_input(names, dob):
    user_details = zip(names, dob)
    dict_details = dict(user_details)
    print(dict_details)
    return dict_details


main()
