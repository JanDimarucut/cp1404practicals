from prac_06.car import Car

MENU = "Menu:\nd) drive\nr) refuel\nq) quit"


def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    my_car = Car(name, 100)
    print(my_car)

    print(MENU)
    menu_choice = input(">>>").lower()

    while menu_choice != "q":
        if menu_choice == "d":
            distance_to_driven = int(input("How many km do you wish to drive? "))

            while distance_to_driven < 0:
                print("Distance must be >= 0")
                distance_to_driven = int(input("How many km do you wish to drive? "))

            distance_driven = my_car.drive(distance_to_driven)
            print("The car drove {}".format(distance_driven))

            if my_car.fuel == 0:
                print("and ran out of fuel")

        elif menu_choice == "r":
            print(my_car)
            add_fuel = int(input("How many units of fuel do you wan to add to the car? "))

            while add_fuel <= 0:
                print("Fuel amount must be > 0")
                add_fuel = int(input("How many units of fuel do you wan to add to the car? "))

            my_car.add_fuel(add_fuel)
            print("Added {} units of fuel".format(add_fuel))

        else:
            print("Invalid choice")

        print(my_car)
        print(MENU)
        menu_choice = input(">>>")
    print("Good bye {}'s driver".format(name))


main()
