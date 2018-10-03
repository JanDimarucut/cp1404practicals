from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Fancy taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("Fare price ${}".format(taxi.get_fare()))


main()
