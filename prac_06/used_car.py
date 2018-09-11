from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("{} {}, {}".format(my_car.name, my_car.fuel, my_car.odometer))
    print("{self.name} {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("My limo", 100)
    # Added 20 units to current fuel
    limo.add_fuel(20)
    print("Current fuel=", limo.fuel)
    print(limo)
    limo.drive(115)
    print("Odometer=", limo.odometer)
    # Fuel remaining after driving
    print("Fuel remaining=", limo.fuel)


main()
