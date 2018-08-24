#import random

#MAX_INCREASE = 0.175  # changed increase from 10% to 17.5%
#MAX_DECREASE = 0.05  # 5%
#MIN_PRICE = 1  # changed price from 0.01 to 1
#MAX_PRICE = 1000.0  # changed the price from 1000 to 100
#INITIAL_PRICE = 10.0
#OUTPUT_FILE = "output_stock"

# Added the output file
#out_file = open(OUTPUT_FILE, 'w')

#day = 0

#price = INITIAL_PRICE
#print("Starting price: ${:,.2f}".format(price), file=out_file)

#while price >= MIN_PRICE and price <= MAX_PRICE:
#    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
#    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
#        price_change = random.uniform(0, MAX_INCREASE)
#    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
#        price_change = random.uniform(-MAX_DECREASE, 0)

#    price *= (1 + price_change)
#    day += 1

#    print("On day {} price is: ${:,.2f}".format(day, price), file=out_file)

# closing output_file
#out_file.close()



import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
print("${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("${:,.2f}".format(price))
