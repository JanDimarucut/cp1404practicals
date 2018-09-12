from prac_06.person_objects import Person


def main():
    people = []

    first_name = input("Enter first name")
    while first_name != '':
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        individual = Person(first_name, last_name, age)
        people.append(individual)
        first_name = input("Enter first name: ")

    for person in people:
        print(person)


main()
