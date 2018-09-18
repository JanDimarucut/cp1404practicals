from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != '':
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        name = input("Name:")
    #    print(add_guitar, "added")

    #    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    #    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}"
                  "{2}".format(i + 1, guitar, vintage_string))
        else:
            print("No vintage guitars")


main()
