from prac_06.date import Date


def main():
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    date = Date(day, month, year)
    print(date)


main()
