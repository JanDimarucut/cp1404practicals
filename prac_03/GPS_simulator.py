"""
Secret population of Golphers that live near the library are 1000
A random gopher is born between 10% of current population and 20%
Each year a random gophers die between 5% and 25%
"""

import random

starting_population = 1000
born = random.uniform(0.1, 0.2)
death = random.uniform(0.05, 0.25)

print("Welcome to the Gopher Population Simulator")
year = 0
print("Starting population: ", round(starting_population))

for i in range(1, 10 + 1):
    year += 1
#random gophers are born
    gophers_born = starting_population * born
#random gophers die
    gophers_died = starting_population * death
#total population of gophers
    total_gophers = starting_population + gophers_born - gophers_died

    starting_population = total_gophers

    print(round(gophers_born), "gophers were born.", round(gophers_died), "died")

    print("Populations: ", round(starting_population))

    print("Year", year)
