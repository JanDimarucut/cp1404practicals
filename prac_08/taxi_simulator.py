from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_06.car import Car

MENU = "Menu:\nq)uit\nc)hoose taxi\nd)rive"


# noinspection PyUnboundLocalVariable
def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    user_input = input(">>>")
    while user_input != "q".lower():
        if user_input == "c".lower():
            print("Taxis available:")

            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))

            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
            print("Bill: ${}".format(total_bill))

        elif user_input == "d".lower():
            current_taxi.start_fare()
            distance_to_drive = int(input("Drive how far?: "))
            while distance_to_drive < 0:
                print("Input has to be > 0")
                distance_to_drive = int(input("Drive how far?: "))
            current_taxi.drive(distance_to_drive)
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            total_bill += current_taxi.get_fare()
            print("Bill: ${}".format(total_bill))

        else:
            print("Invalid options")
        print(MENU)
        user_input = input(">>>")

    print("Total trip cost: ${}".format(total_bill))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
