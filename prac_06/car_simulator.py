from prac_06.car import Car


def main():
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    my_car = Car(car_name, 100)
    print(my_car)

    print("Menu")
    menu_choice = input("d) drive, r) refuel, q) quit")

    while menu_choice != "q":
        if menu_choice == "d":
            distance_driven = int(input("How many km do you wish to drive? "))

            while distance_driven < 0:
                print("Distance must be >= 0")
                distance_driven = int(input("How many km do you wish to drive? "))

            print("The car drove {}".format(distance_driven))
            my_car.drive(distance_driven)
            if my_car.fuel == 0:
                print("and ran out of fuel")

        elif menu_choice == "r":
            print(my_car)
            number_of_units = int(input("How many units of fuel do you wan to add to the car? "))

            while number_of_units == 0:
                print("Fuel amount must be > 0")
                number_of_units = int(input("How many units of fuel do you wan to add to the car? "))

            my_car.add_fuel(number_of_units)
            print("Added {} units of fuel".format(number_of_units))

        else:
            print("Invalid Input")

        print(my_car)
        print("Menu")
        menu_choice = input("d) drive, r) refuel, q) quit")
    print("Good bye {}'s driver".format(car_name))


main()

# my_car = Car("My car", 100)
# my_car.drive(90)
# print("Fuel=", my_car.fuel)
# print("Odometer=", my_car.odometer)
# my_car.add_fuel(50)
# my_car.drive(10)
# print("Fuel=", my_car.fuel)
# print("Odometer=", my_car.odometer)
# print(my_car)
