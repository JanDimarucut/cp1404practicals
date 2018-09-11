from prac_06.guitars import Guitar

def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Second guitar", 1930, 4087.80)
    guitar3 = Guitar("Third guitar", 1990, 80820.30)

    guitars = [guitar1, guitar2, guitar3]
    print("The Antique guitars are:")
    for guitar in guitars:
        if guitar.is_vintage(guitar.get_age()):
            print("{}, {} years old".format(guitar.name, guitar.get_age()))


main()